import streamlit as st

col = 5
row = 6

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

sidebar = st.sidebar

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

column_headers = ["Mån", "Tis", "Ons", "Tors", "Fre"]
columns = st.columns(col)
for i in range(col):
    columns[i].write(f"<div style='text-align: center;'>{column_headers[i]}</div>", unsafe_allow_html=True)

box_width = 130
box_heights = [
    [200, 200, 200, 200, 200],
    [100, 100, 100, 100, 100],
    [100, 50, 100, 100, 90],
    [100, 50, 100, 100, 90],
    [100, 100, 100, 100, 100],
    [100, 200, 100, 100, 100]
]

showBlocks = [
    [block1, block5, block2, block7, block6],
    [block2, block6, block1, block8, block5],
    [block3, ment1, block4, block3, block4],
    [block4, ment2, block3, block4, block3],
    [block5, block7, False, block1, block8],
    [block6, block8, False, block2, block7]
]

incrementPixels = 10

time_bar_html = """
<div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; margin-right: 10px;">
"""

start_hour = 8
start_minute = 20
end_hour = 16
end_minute = 5

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

for j in range(row):
    block_row = st.columns(col)
    for i in range(col):
        if showBlocks[j][i]:
            box_html = f"""
            <div style="width: {box_width}px; height: {box_heights[j][i]}px; border: 1px solid black; background-color: lightblue; padding: 10px; text-align: center;">
            </div>
            """
        else:
            box_html = f"""
            <div style="width: {box_width}px; height: {box_heights[j][i]}px; border: 1px solid black; padding: 10px; text-align: center;">
            </div>
            """
        block_row[i].markdown(box_html, unsafe_allow_html=True)



