import streamlit as st # type: ignore
import api
import plotly.express as px

from models.BloodGroup import BloodGroup

st.write("Welcome to OneDrop Portal")

# st.json(st.user)


blood_donor_col , blood_request_col = st.columns(2)
blood_donors = api.get_all_donors()



with blood_donor_col:
    with st.container():
        st.metric(label="Total Donors", value=len(blood_donors), border = True)

    # Use Enum to get standard blood group order
    bg_counts = {bg.value: 0 for bg in BloodGroup}
    for d in blood_donors:
        bg = d["bloodGroup"]
        if bg in bg_counts:
            bg_counts[bg] += 1

    # Filter out blood groups with 0 donors (optional)
    bg_counts = {k: v for k, v in bg_counts.items() if v > 0}
    bar_fig = px.bar(
        x=list(bg_counts.keys()),
        y=list(bg_counts.values()),
        labels={"x": "Blood Group", "y": "Number of Donors"},
        title="Donor Count by Blood Group"
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    available_count = sum(1 for d in blood_donors if d["available"])
    not_available_count = len(blood_donors) - available_count

    availability_fig = px.bar(
        x=["Available", "Not Available"],
        y=[available_count, not_available_count],
        labels={"x": "Availability", "y": "Number of Donors"},
        title="Donor Availability"
    )
    st.plotly_chart(availability_fig, use_container_width=True)

blood_requests = api.get_all_blood_requests()
with blood_request_col:
    with st.container():
        st.metric(label="Total Blood Requests", value=len(blood_requests), border = True)


