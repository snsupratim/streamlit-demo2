import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Custom CSS to hide Streamlit header, footer, and the "Manage App" button
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}  /* Hides the hamburger menu */
    footer {visibility: hidden;}    /* Hides the footer and "Manage App" button */
    header {visibility: hidden;}    /* Hides the header */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Main app code
st.write("Hello World")
st.write("## This is a H2 Title!")
x = st.text_input("Movie", "Star Wars")

if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")

# Load and display CSV data
data = pd.read_csv("movies.csv")
st.write(data)

# Generate and display bar chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)
