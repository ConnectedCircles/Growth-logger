import pandas as pd
import streamlit as st
import base64

def app():
    
    # Set title and subtitle, additional text
    st.title("Growth Invite Logger V1")
    st.subheader("Property of Connected Circles")
    st.write("""This app allows you to """)
    
    ClientName = st.text_input("Enter client name")
    st.write("Client name entered:", ClientName)

    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file to filter", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        df.insert(0, "Client Name", ClientName)

  

##### DISPLAY OF RESULTS #####
        
        # Display both filtered and unfiltered data in two windows with links to download each below
        st.write(df)
        
        
if __name__ == "__main__":
    app()
