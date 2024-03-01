
from altair import themes
import streamlit as st
import pandas as pd
import numpy as np
from st_pages import Page, show_pages, add_page_title
import streamlit_shadcn_ui as ui
show_pages(
    [
        Page("main.py", "Home"),
        Page("pages/data.py", "Live Data"),
        Page("pages/logs.py", "Logs"),
        Page("pages/record.py", "Analytics"),
    ]
)
table=pd.DataFrame({"Column 1":[1,2,3,4,5,6,7],"Column 2":[11,12,13,14,15,16,17]})
st.title("Energy Monitoring System")
st.header("This is the header")
st.subheader("Hi! I am your subheader")
st.text("Insert some text")
st.markdown("**Hello** *world*") # refer to markdown cheatsheets
st.markdown("---")
cols = st.columns(4)
with cols[0]:
    ui.metric_card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card1")
with cols[1]:
    ui.metric_card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card2")
with cols[2]:
    ui.metric_card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card3")
with cols[3]:
    ui.metric_card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card4")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹ ")
st.table(table)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)