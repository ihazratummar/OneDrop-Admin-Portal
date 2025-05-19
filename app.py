import streamlit as st #type:ignore

# ✅ This must be the first Streamlit command
st.set_page_config(
    page_title="OneDrop Portal",
    page_icon="🩸",
    initial_sidebar_state="expanded",
    layout="wide"
)


# Function for login button
def login():
    if st.button("Login"):
        st.login("google")

# Hide sidebar if not logged in
if not st.user.is_logged_in:
    login()
    st.stop()

# Authorization check
user_email = st.user.email
ALLOWED_EMAILS = set(st.secrets["allowed_emails"])
if user_email not in ALLOWED_EMAILS:
    st.error("You are not authorized to view this page")
    if st.button("Logout"):
        st.logout()
    st.stop()


pages = [
    st.Page("app_pages/home.py", title="Home", icon="🩸"),
    st.Page("app_pages/BloodDonor.py", title="Blood Donors", icon="🩸"),
    st.Page("app_pages/BloodRequests.py", title="Blood Request", icon="🩸"),
    st.Page("app_pages/Report.py", title="Report", icon="🩸"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()

st.sidebar.title(f"Welcome {st.user.name}")
st.logo(st.user.picture)
if st.sidebar.button("Logout"):
    st.logout()
