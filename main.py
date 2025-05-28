import pandas as pd
import plotly.express as px
import streamlit as st

data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(data_url)
    return df

df = load_data()

st.title("Plotly 막대그래프 예제")

st.write("데이터 미리보기:")
st.dataframe(df.head())

# 첫 번째 컬럼을 기준으로 그룹화 후 두 번째 컬럼의 합계 계산 (컬럼명 바꾸기 필요하면 알려줘)
grouped = df.groupby(df.columns[0])[df.columns[1]].sum().reset_index()

# 막대그래프 생성
fig = px.bar(grouped, x=df.columns[0], y=df.columns[1], title=f"{df.columns[0]}별 {df.columns[1]} 합계")

st.plotly_chart(fig)
