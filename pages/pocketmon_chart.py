import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("연도별 포켓몬 출몰 분석 그래프 (2010~2020)")
st.image('pocketmonster_chart.jpg')

data = pd.read_csv("pocket_monsters.csv", encoding='euc-kr',encoding_errors='ignore')
data
if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

with st.sidebar:
    st.caption(f'{ID}님 접속중')
    
with st.form("input"):
    types = st.multiselect("주타입", data['Type 1'].unique())
    legend = st.multiselect("전설의포켓몬(False/True)", data['Legendary'].unique())
    # school = st.multiselect("학교", data['School'].unique())
    submitted = st.form_submit_button("조회")
    
    if submitted:
        name_list = []
        result = data["year"].drop_duplicates().sort_values().reset_index(drop=True)
        
        for re in types:
            for ge in legend:
                name = f"{re}_{ge}"
                name_list.append(name)
                selected_df = data[(data['Type 1'] == re) & (data['Legendary'] == ge)]
                # selected_df = selected_df[["year","num"]].rename(columns={"num": name})
                count_df = selected_df.groupby('year').size().reset_index(name=name)
                
                # 'result' 데이터프레임과 병합
                result = pd.merge(result, count_df, on='year', how='left').sort_values('year')
        result['year'] = result['year'].astype(int)
        st.line_chart(data=result, x='year', y=name_list,use_container_width=True)
        