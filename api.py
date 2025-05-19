import requests
import  os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

API_KEY = os.getenv("ONEDROP_API_KEY")

BASE_URL = "https://api.onedrops.online/api"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def get_all_donors():
    response = requests.get(f"{BASE_URL}/donors/get-donors", headers=headers)
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



