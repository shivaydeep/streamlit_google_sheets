# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
google_sheets_table = conn.read()
dataframe = pd.DataFrame(google_sheets_table)  # Convert Google Sheets table into a pandas dataframe.

# Streamlit content to display the dataframe with images
for index, row in dataframe.iterrows():
    # Assuming the image URL is in a column named "Image"
    st.image(row['Image'], caption=row['Name'])  # Adjust 'Image' and 'Name' to the actual column names in your sheet
    st.write(row.drop('Image'))  # Display other data except for the Image URL

# Alternatively, you can display the entire dataframe as well
st.write(dataframe)
