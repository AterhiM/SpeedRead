import streamlit as st
from src.utils import bionic_reading_try

st.set_page_config(
    page_title="TextPointer - Demo Application",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("<h1 style='text-align: center; color:ushua'>TextPointer: Demo Application</h1>", unsafe_allow_html=True)

st.sidebar.markdown("### About:")

st.sidebar.markdown(
    """This application offers a highlighting technique for speed reading."""
)

default_text = """The heads of UK and US security services have made an unprecedented joint appearance to warn of the threat from China.

FBI director Christopher Wray said China was the "biggest long-term threat to our economic and national security" and had interfered in politics, including recent elections.

MI5 head Ken McCallum said his service had more than doubled its work against Chinese activity in the last three years and would be doubling it again.

MI5 is now running seven times as many investigations related to activities of the Chinese Communist Party compared to 2018, he added.

The FBI's Wray warned that if China was to forcibly take Taiwan it would "represent one of the most horrific business disruptions the world has ever seen".

In response, China Foreign Ministry spokesman Zhao Lijian said British intelligence was trying to "hype up the China threat theory" and he advised the head of MI5 to "cast away imagined demons"."""

input = st.text_area('Enter text here:', value=default_text)
submit = st.button("Highlight !")

# Check to see whether any input text has been inserted
if (len(input.strip()) > 0) and submit:
    bold_text = bionic_reading_try(input)
    st.markdown(bold_text)