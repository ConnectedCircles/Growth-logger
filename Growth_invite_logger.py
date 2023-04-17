import pandas as pd
import streamlit as st
import base64
import datetime

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
        
        
if __name__ == "__main__":
    app()
