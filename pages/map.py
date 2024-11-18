import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속중')
data = pd.read_csv("박물관미술관정보_결측치제거.csv", encoding='euc-kr',encoding_errors='ignore')

st.title('박물관미술관정보')

data = data.copy().fillna(0)
data = data.dropna(subset=['경도', '위도'])
data['color'] = data['박물관미술관구분'].apply(lambda x: '#37eb91' if '사립' in str(x) else '#ff6347')
data

st.map(data, latitude="위도",
       longitude="경도",
    #    size="size",
       color="color")
