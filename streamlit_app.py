# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
google_sheets_table = conn.read()
dataframe = pd.DataFrame(google_sheets_table) # Convert google sheets table into python dataframe. Streamlit expects dataframes as input.

# Define tabs
tab1 = st.tabs(["Table"])

# Streamlit content
with tab1:
  st.write(dataframe)
