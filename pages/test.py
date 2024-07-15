import streamlit as st
import pandas as pd


st.title("SQL 수행평가 응시")
st.write("학번: ", st.session_state["stdnum"])
st.write("이름: ", st.session_state["stdname"])

"### 문제1. a값의 평균과 b값의 평균을 따로 구하는 SQL문을 작성하시오. (10점)"
"(테이블 이름은 table로 한다.)"
df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
st.write(df)
sql = st.text_area("SQL문 입력")

"### 문제2. 다음 SQL문을 실행했을 때 결과를 작성하시오. (10점)"

st.code("SELECT * FROM table WHERE a > 1", language="sql")
sql2 = st.radio("결과2", ["a=2, b=3", "a=3, b=4", "a=4, b=5", "a=5, b=6", "a=6, b=7"])

"### 문제3. 다음 SQL문을 실행했을 때 결과를 작성하시오. (10점)"

st.code("SELECT * FROM table WHERE a > 1 AND b < 5", language="sql")
sql3 = st.radio("결과3", ["a=2, b=3", "a=3, b=4", "a=4, b=5", "a=5, b=6", "a=6, b=7"])

if st.button("제출"):
    if "sql" not in st.session_state:
        st.session_state["sql"] = sql
    if "sql2" not in st.session_state:
        st.session_state["sql2"] = sql2
    if "sql3" not in st.session_state:
        st.session_state["sql3"] = sql3
    st.switch_page("pages/result.py")
