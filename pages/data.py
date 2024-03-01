
import streamlit as st
import pandas as pd
import numpy as np
from st_pages import Page, show_pages, add_page_title
import streamlit_shadcn_ui as ui

#trigger_btn = ui.button(text="Trigger Button", key="trigger_btn")

#ui.alert_dialog(show=trigger_btn, title="Alert Dialog", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog1")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
