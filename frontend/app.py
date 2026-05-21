import streamlit as st

from components.sidebar import (
    render_sidebar
)

from screens.home_screen import (
    show_home
)

from screens.upload_screen import (
    show_upload
)

from screens.dashboard_screen import (
    show_dashboard
)

from screens.insight_screen import (
    show_insights
)

# --------------------------------

st.set_page_config(

    page_title="AI BI Platform",

    layout="wide"
)

# --------------------------------

page = render_sidebar()

# --------------------------------

if page == "Home":

    show_home()

elif page == "Upload Dataset":

    show_upload()

elif page == "Dashboard":

    show_dashboard()

elif page == "AI Insights":

    show_insights()