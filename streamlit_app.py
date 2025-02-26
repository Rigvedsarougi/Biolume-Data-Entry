import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


def append_to_gsheet(data):
    client = get_gspread_client()
    sheet = client.open("Your Google Sheet Name").sheet1  # Replace with your sheet name
    sheet.append_row(data)

# Streamlit UI
st.title("Data Entry App")

# User Inputs
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100)
email = st.text_input("Email")

if st.button("Submit"):
    if name and email:
        append_to_gsheet([name, age, email])
        st.success("Data submitted successfully!")
    else:
        st.error("Please fill all required fields.")

