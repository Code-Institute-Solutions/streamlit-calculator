import streamlit as st
from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.page1 import page1_body
from app_pages.page2 import page2_body

app = MultiPage(app_name= "This is my first App at Streamlit!!!")  # Create an instance

# Add your app pages here using .add_page()
app.add_page("Page 1", page1_body)
app.add_page("Page 2", page2_body)

app.run() # Run the  app