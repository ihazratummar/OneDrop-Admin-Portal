import streamlit as st  # type: ignore
import api
from models.BloodGroup import BloodGroup
from models.NotificationScope import NotificationScope
from models.donors import Donor

raw_donors = api.get_all_donors()

donors = [Donor(**d) for d in raw_donors]


if donors:
    for donor in donors:
        with st.expander(f"{donor.name} ({donor.bloodGroup.value})"):
            st.write(f"**Age:** {donor.age}")
            st.write(f"**Gender:** {donor.gender}")
            st.write(f"**Contact:** {donor.contactNumber}")
            st.write(f"**Email:** {donor.email}")
            st.write(f"**City:** {donor.city}")
            st.write(f"**District:** {donor.district}")
            st.write(f"**State:** {donor.state}")
            st.write(f"**Available:** {'✅' if donor.available else '❌'}")
            st.write(
                f"**Notifications:** {'✅' if donor.notificationEnabled else '❌'} | Scope: {donor.notificationScope.value}")
            #
            #
            #
            with st.form(f"edit_{donor.userId}"):
                name = st.text_input("Name", donor.name)
                age = st.text_input("Age", donor.age)
                gender = st.selectbox("Gender", ["Male", "Female"],
                                      index=["Male", "Female"].index(donor.gender.capitalize()))
                blood_group = st.selectbox("Blood Group", [bg.value for bg in BloodGroup])
                contact = st.text_input("Contact Number", donor.contactNumber)
                city = st.text_input("City", donor.city)
                district = st.text_input("District", donor.district)
                state = st.text_input("State", donor.state)
                email = st.text_input("Email", donor.email)
                available = st.checkbox("Available", donor.available)
                notifications = st.checkbox("Notifications Enabled", donor.notificationEnabled)
                notif_scope = st.selectbox("Notification Scope", [scope.value for scope in NotificationScope])
                #
                submit = st.form_submit_button("💾 Save Changes")
                if submit:
                    updated = Donor(
                        userId=donor.userId,
                        name=name,
                        age=age,
                        gender=gender,
                        bloodGroup=BloodGroup(blood_group).value,
                        city=city,
                        district=district,
                        state=state,
                        available=available,
                        contactNumber=contact,
                        notificationEnabled=notifications,
                        notificationScope=NotificationScope(notif_scope).value,
                        email=email if email else None
                    )
                    api.update_donor(updated.model_dump(mode="json"))
                    st.success("Donor updated ✅")
                    st.rerun()
        #
            if st.button(f"🗑️ Delete {donor.name}", key=f"del_{donor.userId}"):
                api.delete_donor(donor.userId)
                st.warning("Donor deleted ❌")
                st.rerun()
