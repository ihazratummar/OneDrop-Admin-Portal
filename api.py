import requests #type:ignore
import  os
from dotenv import load_dotenv #type:ignore
import streamlit as st #type:ignore


load_dotenv()

API_KEY = os.getenv("ONEDROP_API_KEY")

BASE_URL = "https://api.onedrops.online/api"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


"""
Blood Donor API
"""

def get_all_donors():
    response = requests.get(f"{BASE_URL}/donors/get-donors", headers=headers)
    if response.status_code != 200:
        return []
    return response.json()


def get_donor_by_mobile(mobile):
    response = requests.get(f"{BASE_URL}/donors/search?mobile={mobile}", headers=headers)
    return response.json()

def update_donor(data: dict):
    url = f"{BASE_URL}/donors/create-update-donor"
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


def delete_donor(user_id: str):
    url = f"{BASE_URL}/donors/delete-donor"
    params = {"userId": user_id}
    response = requests.delete(url, headers=headers, params=params)

    if response.status_code != 200:
        st.error(f"Error deleting donor: {response.status_code} - {response.text}")
        response.raise_for_status()

    return response.json()

"""
Blood Request API
"""

def get_all_blood_requests():
    response = requests.get(f"{BASE_URL}/blood-request/get-blood-requests", headers=headers)
    if response.status_code != 200:
        return []
    return response.json()

def delete_blood_request(request_id: str):
    url = f"{BASE_URL}/blood-request/delete-blood-request"
    params = {"bloodRequestId": request_id}
    response = requests.delete(url, headers=headers, params=params)

    if response.status_code != 200:
        st.error(f"Error deleting blood request: {response.status_code} - {response.text}")
        response.raise_for_status()

def update_blood_request_status(request_id: str, status: str):
    url = f"{BASE_URL}/blood-request/status"
    params = {"bloodRequestId": request_id}
    response = requests.patch(url, headers=headers, params=params, json = {"bloodRequestStatus": status})

    if response.status_code != 200:
        st.error(f"Error updating blood request status: {response.status_code} - {response.text}")
        response.raise_for_status()


"""
Report API
"""



def get_all_reports():
    response = requests.get(f"{BASE_URL}/report/all-reports", headers=headers)
    response.raise_for_status()
    if response.status_code != 200:
        return []
    return response.json()

def update_report_status(report_id: str, status: str):
    url = f"{BASE_URL}/report/status"
    params = {"reportId": report_id}
    response = requests.patch(url, headers=headers, params=params, json = {"reportStatus": status})

    if response.status_code != 200:
        st.error(f"Error updating report status: {response.status_code} - {response.text}")
        response.raise_for_status()

def delete_report(report_id: str):
    url = f"{BASE_URL}/report/delete"
    params = {"reportId": report_id}
    response = requests.delete(url, headers=headers, params=params)

    if response.status_code != 200:
        st.error(f"Error deleting report: {response.status_code} - {response.text}")
        response.raise_for_status()

