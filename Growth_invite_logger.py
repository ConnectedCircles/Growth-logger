import pandas as pd
import streamlit as st
import base64
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("growth-logger-f8043abda96b.json", scope)
client = gspread.authorize(creds)

# Define function to append data to Google Sheet
def append_to_sheet(df):
    # Open the Google Sheet
    sheet = client.open("Invited Profiles").worksheet("Invited")
    # Append the data to the sheet
    sheet.insert_rows(df.values.tolist())

def app():
    
    # Set title and subtitle, additional text
    st.title("Growth Invite Logger V1")
    st.subheader("Property of Connected Circles")
    st.write("""This app allows you to """)
    
    # Set client name, invite date and category
    ClientName = st.text_input("Enter client name")
    DateInvited = st.date_input("Select a date", datetime.date.today())
    Category = st.text_input("Enter category")


    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file to filter", type="csv")
    
    # Process data
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    
        # Create a column for the name of the client
        df.insert(0, "Client Name", ClientName)
        # Rewrite the date and category columns
        df["Date collected"] = DateInvited
        df["Category"] = Category

        ##### DISPLAY OF RESULTS #####
        
        # Display both filtered and unfiltered data in two windows with links to download each below
        st.write(df)

        # Button to append data to Google Sheet
        if st.button("Append data to Google Sheet"):
            append_to_sheet(df.dropna(how="all", axis=1))

if __name__ == "__main__":
    app()
