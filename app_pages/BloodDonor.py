import streamlit as st
import time
import api
from models.BloodGroup import BloodGroup
from models.NotificationScope import NotificationScope


donors = api.get_all_donors()


def rerun():
    st.experimental_set_query_params(refresh=str(hash(time.time())))


if donors:
    for donor in donors:
        with st.expander(f"{donor['name']} ({donor['bloodGroup']})"):
            st.write(f"**Age:** {donor['age']}")
            st.write(f"**Gender:** {donor['gender']}")
            st.write(f"**Contact:** {donor['contactNumber']}")
            st.write(f"**Email:** {donor.get('email', 'N/A')}")
            st.write(f"**City:** {donor['city']}")
            st.write(f"**District:** {donor['district']}")
            st.write(f"**State:** {donor['state']}")
            st.write(f"**Available:** {'✅' if donor['available'] else '❌'}")
            st.write(
                f"**Notifications:** {'✅' if donor['notificationEnabled'] else '❌'} | Scope: {donor['notificationScope']}")



            with st.form(f"edit_{donor['userId']}"):
                name = st.text_input("Name", donor['name'])
                age = st.text_input("Age", donor['age'])
                gender = st.selectbox("Gender", ["Male", "Female"],
                                      index=["Male", "Female"].index(donor['gender']))
                blood_group = st.selectbox("Blood Group", [bg.value for bg in BloodGroup])
                contact = st.text_input("Contact Number", donor['contactNumber'])
                city = st.text_input("City", donor['city'])
                district = st.text_input("District", donor['district'])
                state = st.text_input("State", donor['state'])
                email = st.text_input("Email", donor['email'])
                available = st.checkbox("Available", donor['available'])
                is_private = st.checkbox("Private Contact Number", donor['isContactNumberPrivate'])
                notifications = st.checkbox("Notifications Enabled", donor['notificationEnabled'])
                notif_scope = st.selectbox("Notification Scope", [scope.value for scope in NotificationScope])

                submit = st.form_submit_button("💾 Save Changes")
                if submit:
                    updated = {
                        "userId": donor["userId"],
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "bloodGroup": blood_group,
                        "city": city,
                        "district": district,
                        "state": state,
                        "available": available,
                        "contactNumber": contact,
                        "isContactNumberPrivate": is_private,
                        "notificationEnabled": notifications,
                        "notificationScope": notif_scope,
                        "email": email
                    }
                    api.update_donor(updated)
                    st.success("Donor updated ✅")
                    rerun()

            if st.button(f"🗑️ Delete {donor['name']}", key=f"del_{donor['userId']}"):
                api.delete_donor(donor["userId"])
                st.warning("Donor deleted ❌")
                rerun()

