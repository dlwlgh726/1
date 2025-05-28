import pandas as pd
import plotly.express as px
import streamlit as st
pip install plotly

# 데이터 URL (직접 다운로드 링크)
data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv(data_url)
    return df

df = load_data()

st.title("Plotly 시각화 예제")

st.write("데이터 미리보기:")
st.dataframe(df.head())

# 예시: 데이터의 첫 두 컬럼으로 산점도 그리기 (컬럼명에 따라 수정 필요)
fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title="Scatter plot of first two columns")
st.plotly_chart(fig)
