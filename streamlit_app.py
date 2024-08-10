# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
google_sheets_table = conn.read()
dataframe = pd.DataFrame(google_sheets_table)  # Convert Google Sheets table into a pandas dataframe.

# Streamlit content to display the dataframe
st.write(dataframe)
