import streamlit as st

# 5 columns for all days on a school week. 93 rows, one for each five minute interval on a school day.
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

# The actuall code to show all the boxes. It itterates through all boxes and checks if it should be vissible.
for j in range(row):
    block_row = st.columns(col)
    for i in range(col):
        #If the box is vissible we create it using HTML an the previously set variables on heights and names.
        #if showBlocks[j][i]:
        boxHtml = f"""
        <div style="width: 130px; height: 2px; border: 0px solid black; background-color: lightgrey; padding: 0px; text-align: center;">
        </div>
        """
        #If the box is hidden it should create an invissible or in this case barely vissible outline of where that block. This ensures the other boxes are at the same place all the time.
        #else:
        #    boxHtml = f"""
        #    <div style="width: {boxWidth}px; height: {boxHeights[j][i]}px; border: 1px solid black; padding: 10px; opacity: 0.1; text-align: center;">
        #    </div>
        #    """
        block_row[i].markdown(boxHtml, unsafe_allow_html=True)