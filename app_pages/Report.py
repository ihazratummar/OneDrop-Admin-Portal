import streamlit as st
from datetime import datetime
import api
from models.report_model import ReportModel, ReportStatus
from utils.utils import confirm_dialog

st.title("Report")

raw_report = api.get_all_reports()

reports = [ReportModel(**r) for r in raw_report]


def delete_report_request_by_id(report_id):
    api.delete_report(report_id)
    st.success("Report deleted ✅")


if reports:
    for report in reports:
        with st.expander(f"{report.reportedName} - **Status:** {report.reportStatus.value}"):
            left_col, right_col = st.columns(2)

            with left_col:
                st.write(f"**Reason:** {report.reason}")
                st.write(f"**Description:** {report.description}")
                timestamp_str = report.timestamp
                dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                formatted_dt = dt.strftime("%d %B %Y")
                st.write(f"**Date:** {formatted_dt}")
                st.write(f"**NUmber:** {report.reportedMobileNumber}")
                if report.screenshot and report.screenshot != "null":
                    st.image(report.screenshot)

            with right_col:
                with st.form(f"edit_{report.reportId}"):
                    status = st.selectbox("Status", [s.value for s in ReportStatus])
                    submit = st.form_submit_button("💾 Save Changes")
                    if submit:
                        api.update_report_status(report.reportId, status=status)
                        st.success("Report updated ✅")
                        st.rerun()

                button_key = f"delete_btn_{report.reportId}"
                dialog_key = f"confirm_delete_{report.reportId}"

                if st.button("🗑️ Delete", key=button_key):
                    st.session_state["delete_report_target_id"] = report.reportId
                    st.session_state[dialog_key] = True
                    st.rerun()

                confirm_dialog(
                    title="Confirm Delete",
                    message="Are you sure you want to delete this blood request?",
                    on_confirm=lambda: delete_report_request_by_id(st.session_state["delete_report_target_id"]),
                    state_key=dialog_key
                )
