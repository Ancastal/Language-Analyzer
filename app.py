import streamlit as st
from hsk_profiler import profile

# Set page title and subtitle
st.set_page_config(page_title="HSK Profiler", page_icon=":book:", layout="wide")
st.title("HSK Profiler")
st.subheader("Analyze the HSK level of Chinese text")

# Add text area and button
txt = st.text_area("Enter Chinese text here:")
if st.button('Profile', key="profile", help="Analyze the text and display the results."):

    # Analyze text and display results
    total_chars, hsk_counts, avg_hsk_level = profile(txt)
    st.write("Total characters:", total_chars)
    st.write("HSK level counts:", hsk_counts)
    st.write("Average HSK level:", avg_hsk_level)

    # Create bar chart of HSK level distribution
    hsk_data = {"HSK Level " + str(i): hsk_counts[i-1] for i in range(1, 7)}
    st.bar_chart(hsk_data)

# Define CSS styles
STYLE = """
<style>
body {
    background-color: #f9f9f9;
}
button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 18px;
}
button:hover {
    background-color: #3e8e41;
}
textarea {
    height: 300px;
    border-radius: 4px;
    border: 1px solid #ccc;
    padding: 12px 20px;
    box-sizing: border-box;
    font-size: 18px;
    resize: vertical;
}
</style>
"""

# Add CSS styles to page
st.markdown(STYLE, unsafe_allow_html=True)
