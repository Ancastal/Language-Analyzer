import streamlit as st
from streamlit_option_menu import option_menu
from website_class import Website

st.set_page_config(page_title="Linguistic Analysis", page_icon=":book:", layout="wide")
selected = option_menu(None, ["Home", "HSK Profiler", "Readability", "BLEU Scores" , "About"], orientation="horizontal")

website = Website(st)
# Set page title and subtitle
if selected == "HSK Profiler":
    website.show_hsk_profiler()
elif selected == "Readability":
    website.show_readability()
elif selected == "BLEU Scores":
    website.show_bleu()
else:
    website.show_home()
