import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_calculator import calculator_body

app = MultiPage(app_name="Calculator App")  # Create an instance of the app


# Add your app pages here using .add_page()
app.app_page("Calculator", calculator_body)

app.run()
