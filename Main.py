import streamlit as st

st.title("SQL 수행평가")

stdnum = st.text_input("학번")
stdname = st.text_input("이름")

if st.button("save"):
    if "stdnum" not in st.session_state:
        st.session_state["stdnum"] = stdnum
    if "stdname" not in st.session_state:
        st.session_state["stdname"] = stdname
    st.switch_page("pages/test.py")
