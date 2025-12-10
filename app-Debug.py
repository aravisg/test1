# 2025-12-10

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title("Google Sheets Debug Mode")

st.write("### Step 1: Check if secrets loaded")
try:
    st.write(st.secrets["google_service_account"]["client_email"])
except Exception as e:
    st.error("❌ Google service account JSON NOT LOADED")
    st.stop()

st.success("✔ Secrets loaded")

# Prepare credentials
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

st.write("### Step 2: Try creating credentials")
try:
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        st.secrets["google_service_account"], scope
    )
    st.success("✔ Credentials object created")
except Exception as e:
    st.error(f"❌ Credentials creation failed: {e}")
    st.stop()

# Authorize
st.write("### Step 3: Try Google authorization")
try:
    client = gspread.authorize(credentials)
    st.success("✔ Authorized successfully")
except Exception as e:
    st.error(f"❌ Authorization failed: {e}")
    st.stop()

# Check sheet ID
sheet_id = st.secrets["sheets"]["sheet_id"]
st.write("### Step 4: Using Sheet ID:", sheet_id)

try:
    st.write("Listing files in Drive...")
    files = client.list_spreadsheet_files()
    st.write(files)
except Exception as e:
    st.write("Drive listing error:", e)

# Test reading sheet metadata
st.write("### Step 5: Try accessing sheet")
try:
    spreadsheet = client.open_by_key(sheet_id)
    st.success("✔ Sheet opened successfully (permissions OK!)")
    
    sheet = spreadsheet.sheet1
    st.write("First row:", sheet.row_values(1))

except Exception as e:
    st.error("❌ Cannot access sheet — Permission or Sheet ID issue")
    st.error(str(e))
    st.stop()

st.success("🎉 Debug Passed: You have full access!")
