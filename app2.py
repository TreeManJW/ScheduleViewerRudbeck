import streamlit as st

# 5 columns for all days on a school week. 93 rows, one for each minute on a school day.
col = 5
row = 93

columns = st.columns(col)
sidebar = st.sidebar

columnHeaders = ["Mån", "Tis", "Ons", "Tors", "Fre"]

time_bar_html = """
<div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; margin-right: 10px;">
"""

#Writing the day heathers.
for i in range(col):
    columns[i].write(f"<div style='text-align: center;'>{columnHeaders[i]}</div>", unsafe_allow_html=True)