# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Load data from the Excel file
file_path = '/mnt/data/TOP 5 QR Code generator & Feature comparison.xlsx'
dataframe = pd.read_excel(file_path)

# Streamlit content to display the dataframe
st.write(dataframe)
