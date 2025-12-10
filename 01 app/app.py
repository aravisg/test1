# 2025-12-09

import streamlit as st
from database import *

# Create table on startup
create_table()

st.title("Contact Manager (Streamlit + SQLite)")

menu = ["Add Contact", "View Contacts", "Update Contact", "Delete Contact"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- ADD -------------------
if choice == "Add Contact":
    st.subheader("Add a new contact")
    name = st.text_input("Name")
    contact = st.text_input("Contact Number")
    email = st.text_input("Email")
    notes = st.text_area("Notes")

    if st.button("Add"):
        add_contact(name, contact, email, notes)
        st.success("Contact added successfully!")

# ---------------- VIEW -------------------
elif choice == "View Contacts":
    st.subheader("All Contacts")
    rows = get_all_contacts()
    st.table(rows)

# ---------------- UPDATE -------------------
elif choice == "Update Contact":
    st.subheader("Update Contact")
    rows = get_all_contacts()
    ids = [row[0] for row in rows]

    selected_id = st.selectbox("Select ID to update", ids)
    selected_row = [r for r in rows if r[0] == selected_id][0]

    new_name = st.text_input("Name", selected_row[1])
    new_contact = st.text_input("Contact", selected_row[2])
    new_email = st.text_input("Email", selected_row[3])
    new_notes = st.text_area("Notes", selected_row[4])

    if st.button("Update"):
        update_contact(selected_id, new_name, new_contact, new_email, new_notes)
        st.success("Contact updated successfully!")

# ---------------- DELETE -------------------
elif choice == "Delete Contact":
    st.subheader("Delete Contact")
    rows = get_all_contacts()
    ids = [row[0] for row in rows]

    delete_id = st.selectbox("Select ID to delete", ids)

    if st.button("Delete"):
        delete_contact(delete_id)
        st.warning("Contact deleted!")
