# 2025-12-10

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import uuid

# --- Google Sheets Auth ---
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["google_service_account"], scope
)

client = gspread.authorize(credentials)
sheet = client.open_by_key(st.secrets["sheets"]["sheet_id"]).sheet1


# --- Helper functions ---
def load_data():
    records = sheet.get_all_records()
    return pd.DataFrame(records)


def add_record(name, contact, email, notes):
    row_id = str(uuid.uuid4())
    sheet.append_row([name, contact, email, notes, row_id])


def delete_record(row_id):
    df = load_data()
    idx = df.index[df["id"] == row_id]
    if len(idx) > 0:
        sheet.delete_rows(idx[0] + 2) 


def update_record(row_id, name, contact, email, notes):
    df = load_data()
    idx = df.index[df["id"] == row_id]
    if len(idx) > 0:
        row_num = idx[0] + 2
        sheet.update(f"A{row_num}:E{row_num}", [[name, contact, email, notes, row_id]])


# --- UI Begins ---
st.title("Contact Manager (Google Sheets Backend)")

menu = st.radio("Choose action", ["Add", "List / Update / Delete"])

if menu == "Add":
    st.subheader("Add New Contact")
    name = st.text_input("Name")
    contact = st.text_input("Contact Number")
    email = st.text_input("Email")
    notes = st.text_area("Notes")

    if st.button("Save"):
        add_record(name, contact, email, notes)
        st.success("Record added.")

else:
    st.subheader("All Contacts")
    df = load_data()
    st.dataframe(df)

    st.subheader("Update / Delete")

    selected_id = st.selectbox("Select ID", df["id"].tolist())

    row = df[df["id"] == selected_id].iloc[0]

    new_name = st.text_input("Name", row["name"])
    new_contact = st.text_input("Contact", row["contact"])
    new_email = st.text_input("Email", row["email"])
    new_notes = st.text_area("Notes", row["notes"])

    if st.button("Update"):
        update_record(selected_id, new_name, new_contact, new_email, new_notes)
        st.success("Updated.")

    if st.button("Delete"):
        delete_record(selected_id)
        st.error("Deleted.")
