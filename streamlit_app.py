# Import python packages
import streamlit as st
import os
from snowflake.snowpark.context import get_active_session

# set layout as wide to extend width to full size
st.set_page_config(layout="wide")

# session initialization
session = get_active_session()

# contents to display
st.title(f"Demo Streamlit App")