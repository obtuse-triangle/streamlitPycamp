import streamlit as st
import pandas as pd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if not firebase_admin._apps:
    import json

    key_dict = json.loads(st.secrets["textkey"])
    creds = credentials.Certificate(key_dict)
    firebase_admin.initialize_app(creds)

ref = db.reference("abc", url="https://pycamp-2ff06-default-rtdb.firebaseio.com/")

arr = []
for i in ref.get().keys():
    arr.append(ref.get()[i])

df = pd.DataFrame([i for i in arr], columns=["stdnum", "stdname", "score", "question"])

"# SQL 수행평가 결과"

st.write(df)

import matplotlib.pyplot as plt

# question = [0, 0, 0]
# for i in range(len(df)):
#     question[0] += df["question"][i][0]
#     question[1] += df["question"][i][1]
#     question[2] += df["question"][i][2]

# plt.bar(["q1", "q2", "q3"], question)
# plt.title("score by question")

# st.pyplot(plt)

# 문제별 평균 with matplotlib
avg = [0, 0, 0]
for i in range(len(df)):
    avg[0] += df["question"][i][0]
    avg[1] += df["question"][i][1]
    avg[2] += df["question"][i][2]

avg = [i / len(df) for i in avg]
plt.bar(["q1", "q2", "q3"], avg)
plt.title("avg score by question")

st.pyplot(plt)
