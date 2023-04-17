import pandas as pd
import streamlit as st
import base64

def app():
    
    # Set title and subtitle, additional text
    st.title("Growth Invite Logger V1")
    st.subheader("Property of Connected Circles")
    st.write("""This app allows you to filter lists of profiles by seniority. By default, it uses a set of keywords to detect and filter CXO+ level profiles 
    (incl. partners and VPs etc.). It uses 2 sets of keywords, one that is case-sensitive and one that is case insensitive. This avoids errors such as the 
    inclusion of 'aCCOunt managers' when searching for 'CCO'. Both sets of keywords are fully customizable and keywords can be added or removed. Keywords must 
    be separated by a comma, whitespace will be considered a part of a keyword. You can preview the both the labeled and filtered data in the two preview 
    windows below. You can download the data either labeled, filtered or filtered profile URLs only, all as a .csv""")
    
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file to filter", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        
        
if __name__ == "__main__":
    app()
