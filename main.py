import streamlit as st
import pandas as pd

st.title("Today's menu")

# data = {
#     '과일': ['사과', '바나나', '체리', '데이트', '엘더베리'],
#     '수량': [10, 15, 20, 25, 30],
#     '가격': [0.5, 0.25, 0.75, 1.0, 2.0]
# }
# df = pd.DataFrame(data)

df = pd.read_excel('menu2.xlsx', header=2, index_col=None)
df.drop(['Unnamed: 0'], axis = 1, inplace = True)

st.dataframe(df)