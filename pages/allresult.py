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

question = [0, 0, 0]
for i in range(len(df)):
    question[0] += df["question"][i][0]
    question[1] += df["question"][i][1]
    question[2] += df["question"][i][2]

plt.figure().patch.set_facecolor("dimgray")
plt.gca().set_facecolor("dimgray")
plt.bar(["q1", "q2", "q3"], question, color="darkgrey")
"## 문제별 합산점수"
st.pyplot(plt)

plt.close()

# 문제별 평균 with matplotlib
avg = [0, 0, 0]
for i in range(len(df)):
    avg[0] += df["question"][i][0]
    avg[1] += df["question"][i][1]
    avg[2] += df["question"][i][2]

avg = [i / len(df) for i in avg]
plt.figure().patch.set_facecolor("dimgray")
plt.gca().set_facecolor("dimgray")
plt.bar(["q1", "q2", "q3"], avg, color="darkgrey")
"## 문제별 평균점수"

st.pyplot(plt)

plt.close()

# 문제별 표준편차 with matplotlib
import numpy as np

"## 문제별 표준편차"

std = [0, 0, 0]
for i in range(len(df)):
    std[0] += (df["question"][i][0] - avg[0]) ** 2
    std[1] += (df["question"][i][1] - avg[1]) ** 2
    std[2] += (df["question"][i][2] - avg[2]) ** 2

std = [np.sqrt(i / len(df)) for i in std]
plt.figure().patch.set_facecolor("dimgray")
plt.gca().set_facecolor("dimgray")
plt.bar(["q1", "q2", "q3"], std, color="darkgrey")
st.pyplot(plt)
