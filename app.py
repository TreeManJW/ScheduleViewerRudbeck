import streamlit as st

# 5 columns for all days on a school week. 6 rows, one for each block on a day.
col = 5
row = 6

columns = st.columns(col)
sidebar = st.sidebar

columnHeaders = ["Mån", "Tis", "Ons", "Tors", "Fre"]

# Variables to create lines with 5 minute, 10 pixels increments that range from 8:20 to 16:05. The longest possible day.
incrementPixels = 10
start_hour = 8
start_minute = 20
end_hour = 16
end_minute = 5

time_bar_html = """
<div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; margin-right: 10px;">
"""

# Variables that you can change with the sidebar and that are used to check if the block should be vissible.
block1 = True
block2 = True
block3 = True
block4 = True
block5 = True
block6 = True
block7 = True
block8 = True
ment1 = True
ment2 = True

#Setting the with, height, name, and vissibility of every single box.
boxWidth = 130
boxHeights = [
    [200, 200, 200, 200, 200],
    [100, 100, 100, 100, 100],
    [100, 50, 100, 100, 90],
    [100, 50, 100, 100, 90],
    [100, 100, 100, 100, 100],
    [100, 200, 100, 100, 100]
]
boxNames = [
    ["1", "5", "2", "7", "6"],
    ["2", "6", "1", "8", "5"],
    ["3", "M1", "4", "3", "4"],
    ["4", "M2", "3", "4", "3"],
    ["5", "7", "", "1", "8"],
    ["6", "8", "", "2", "7"]
]
showBlocks = [
    [block1, block5, block2, block7, block6],
    [block2, block6, block1, block8, block5],
    [block3, ment1, block4, block3, block4],
    [block4, ment2, block3, block4, block3],
    [block5, block7, False, block1, block8],
    [block6, block8, False, block2, block7]
]

#Setting up the sidebar.
block1 = sidebar.checkbox("Block 1", value=block1)
block2 = sidebar.checkbox("Block 2", value=block2)
block3 = sidebar.checkbox("Block 3", value=block3)
block4 = sidebar.checkbox("Block 4", value=block4)
block5 = sidebar.checkbox("Block 5", value=block5)
block6 = sidebar.checkbox("Block 6", value=block6)
block7 = sidebar.checkbox("Block 7", value=block7)
block8 = sidebar.checkbox("Block 8", value=block8)
ment1 = sidebar.checkbox("Ment 1", value=ment1)
ment2 = sidebar.checkbox("Ment 2", value=ment2)

#Writing the day heathers.
for i in range(col):
    columns[i].write(f"<div style='text-align: center;'>{columnHeaders[i]}</div>", unsafe_allow_html=True)

# Shit I will fix later.
current_hour = start_hour
current_minute = start_minute

while current_hour < end_hour or (current_hour == end_hour and current_minute <= end_minute):
    time_bar_html += f"""<div style="height: 1px; background-color: #ccc; margin-bottom: {incrementPixels}px; opacity: 0.1;"></div>"""

    current_minute += 5
    if current_minute >= 60:
        current_minute -= 60
        current_hour += 1

time_bar_html += "</div>"
st.markdown(time_bar_html, unsafe_allow_html=True)

# The actuall code to show all the boxes. It itterates through all boxes and checks if it should be vissible.
for j in range(row):
    block_row = st.columns(col)
    for i in range(col):
        #If the box is vissible we create it using HTML an the previously set variables on heights and names.
        if showBlocks[j][i]:
            boxHtml = f"""
            <div style="width: {boxWidth}px; height: {boxHeights[j][i]}px; border: 1px solid black; background-color: lightblue; padding: 10px; text-align: center;">
            {boxNames[j][i]}
            </div>
            """
        #If the box is hidden it should create an invissible or in this case barely vissible outline of where that block. This ensures the other boxes are at the same place all the time.
        else:
            boxHtml = f"""
            <div style="width: {boxWidth}px; height: {boxHeights[j][i]}px; border: 1px solid black; padding: 10px; opacity: 0.1; text-align: center;">
            </div>
            """
        block_row[i].markdown(boxHtml, unsafe_allow_html=True)



