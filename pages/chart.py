import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("박물관미술관정보_결측치제거.csv", encoding='euc-kr',encoding_errors='ignore')

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

with st.sidebar:
    st.caption(f'{ID}님 접속중')
    
with st.form("input"):
    partition = st.multiselect("박물관미술관구분", data['박물관미술관구분'].unique())
    관리기관 = st.multiselect("관리기관명", data['관리기관명'].unique())
    # school = st.multiselect("학교", data['School'].unique())
    submitted = st.form_submit_button("조회")
    
    if submitted:
        name_list = []
        result = data["청소년관람료"].drop_duplicates().sort_values().reset_index(drop=True)
        
        for re in partition:
            for ge in 관리기관:
                # for sc in school:
                name = f"{re}_{ge}"
                name_list.append(name)
                selected_df = data[(data['박물관미술관구분'] == re) & (data['관리기관명'] == ge)]
                selected_df = selected_df[["청소년관람료","어른관람료"]].rename(columns={"어른관람료": name})
                result = pd.merge(result, selected_df, on='청소년관람료').sort_values('청소년관람료')
        
        st.line_chart(data=result, x='청소년관람료', y=name_list,use_container_width=True)
        