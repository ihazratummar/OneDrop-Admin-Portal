import streamlit as st  # type:ignore

import api
from models.BloodRequestModel import BloodRequestModel, BloodRequestStatus
from utils.utils import time_count_down, get_time_from_milis, confirm_dialog

st.title("Blood Requests")

raw_blood_requests = api.get_all_blood_requests()

blood_requests = [BloodRequestModel(**br) for br in raw_blood_requests]


def delete_request_by_id(blood_id):
    api.delete_blood_request(blood_id)
    st.success("Blood request deleted ✅")

if blood_requests:
    for blood_request in blood_requests:
        with st.expander(f"{blood_request.patientName} ({blood_request.patientBloodGroup.value})"):
            st.write(f"**Contact Person:** {blood_request.contactPersonName}")
            st.write(f"**Age:** {blood_request.patientAge}")
            st.write(
                f"**Location:** {blood_request.hospitalName} , {blood_request.patientCity}, {blood_request.patientDistrict}, {blood_request.patientState}")
            st.write(f"**Status:** {blood_request.bloodRequestStatus.value}")

            col1, col2 = st.columns(2)
            with col1:
                st.write("**Time Remaining:**")
                time_count_down(blood_request.date)
            with col2:
                st.write("**Creation Date:**")
                date = get_time_from_milis(blood_request.dateOfCreation)
                st.write(date)
            if blood_request.requisitionForm:
                st.image(blood_request.requisitionForm)

            button_key = f"delete_btn_{blood_request.id}"
            dialog_key = f"confirm_delete_{blood_request.id}"

            if st.button("🗑️ Delete", key=button_key):
                st.session_state["delete_target_id"] = blood_request.id
                st.session_state[dialog_key] = True
                st.rerun()



            with st.form(f"edit_{blood_request.id}"):
                status = st.selectbox("Status", [s.value for s in BloodRequestStatus])
                submit = st.form_submit_button("💾 Save Changes")
                if submit:
                    api.update_blood_request_status(blood_request.id, status=status)
                    st.success("Blood request updated ✅")
                    st.rerun()

            # Always place this at the end of your item block
            confirm_dialog(
                title="Confirm Delete",
                message="Are you sure you want to delete this blood request?",
                on_confirm=lambda: delete_request_by_id(st.session_state["delete_target_id"]),
                state_key=dialog_key
            )


