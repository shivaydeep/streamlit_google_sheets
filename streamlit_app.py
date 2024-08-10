import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
google_sheets_table = conn.read()  # Read data normally
dataframe = pd.DataFrame(google_sheets_table)  # Convert Google Sheets table into a pandas dataframe.

# If the first row should be part of the data:
dataframe.columns = dataframe.iloc[0]  # Set the first row as headers
dataframe = dataframe[1:].reset_index(drop=True)  # Drop the first row from data and reset the index

# Streamlit content to display the dataframe with images
for index, row in dataframe.iterrows():
    st.image(row['Image'], caption=row['Name'])  # Adjust based on actual column names
    st.write(row.drop('Image'))  # Display other data except for the Image URL

# Alternatively, you can display the entire dataframe as well
st.write(dataframe)
