import streamlit as st

st.title("SQL 수행평가 결과 확인")

st.write("학번: ", st.session_state["stdnum"])
st.write("이름: ", st.session_state["stdname"])
score = 0

question = [0, 0, 0]


"### 문제1. a값의 평균과 b값의 평균을 따로 구하는 SQL문을 작성하시오. (10점)"
if st.session_state["sql"].lower() == "SELECT AVG(a), AVG(b) FROM table".lower():
    ":white_check_mark:"
    question[0] = 10
else:
    ":no_entry_sign:"
"#### 학생답안"
st.code(st.session_state["sql"], language="sql")
"#### 정답"
st.code("SELECT AVG(a), AVG(b) FROM table", language="sql")

"### 문제2. 다음 SQL문을 실행했을 때 결과를 작성하시오. (10점)"
if st.session_state["sql2"] == "a=3, b=4":
    ":white_check_mark:"
    question[1] = 10
else:
    ":no_entry_sign:"
"#### 학생답안"
st.code(st.session_state["sql2"], language="sql")
"#### 정답"
st.code("a=3, b=4", language="sql")

"### 문제3. 다음 SQL문을 실행했을 때 결과를 작성하시오. (10점)"
if st.session_state["sql3"] == "a=3, b=4":
    ":white_check_mark:"
    question[2] = 10
else:
    ":no_entry_sign:"
"#### 학생답안"
st.code(st.session_state["sql3"], language="sql")
"#### 정답"
st.code("a=3, b=4", language="sql")

st.write("## 점수: ", sum(question))

if st.button("다른 학생의 결과도 확인해보기", type="primary"):
    st.switch_page("pages/allresult.py")


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if not firebase_admin._apps:
    import json

    key_dict = json.loads(st.secrets["textkey"])
    creds = credentials.Certificate(key_dict)
    firebase_admin.initialize_app(creds)

    # cred = credentials.Certificate("./secret.json")
    # firebase_admin.initialize_app(cred)

ref = db.reference("abc", url="https://pycamp-2ff06-default-rtdb.firebaseio.com/")

# Read the data at the posts reference (this is a blocking operation)
ref.push(
    {
        "stdnum": st.session_state["stdnum"],
        "stdname": st.session_state["stdname"],
        "score": sum(question),
        "question": question,
    }
)
