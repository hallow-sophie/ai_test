import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"


ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속중')
data = pd.read_csv("pocket_monsters.csv", encoding='euc-kr',encoding_errors='ignore')

st.title('Pocketmonster 분포\n (2010~2020 한국 출몰지역 분석 data)')
st.image('pocketmonster_bg.jpg')
data
# data = data.copy().fillna(0)
# data = data.dropna(subset=['경도', '위도'])
data['color'] = data['Legendary'].apply(lambda x: '#37eb91' if 'True' in str(x) else '#ff6347')


st.map(data, latitude="latitude",
       longitude="longitude",
    #    size="size",
       color="color")
