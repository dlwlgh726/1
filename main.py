import pandas as pd
import plotly.express as px
import streamlit as st

data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(data_url)
    return df

df = load_data()

st.title("Plotly 막대그래프 선택형")

st.write("데이터 미리보기:")
st.dataframe(df.head())

x_col = st.selectbox("X축으로 사용할 컬럼을 선택하세요", options=df.columns)
y_col = st.selectbox("Y축으로 사용할 컬럼을 선택하세요", options=df.columns)

# 그룹화 후 y값 합산, reset_index에 name 인자 추가로 컬럼명 중복 방지
grouped = df.groupby(x_col)[y_col].sum().reset_index(name=f"{y_col}_sum")

fig = px.bar(grouped, x=x_col, y=f"{y_col}_sum", title=f"{x_col}별 {y_col} 합계")

st.plotly_chart(fig)
