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

# x축, y축 컬럼 선택 위젯
x_col = st.selectbox("X축으로 사용할 컬럼을 선택하세요", options=df.columns)
y_col = st.selectbox("Y축으로 사용할 컬럼을 선택하세요", options=df.columns)

# y축은 수치형이어야 하니까 필터링 한번 해볼 수도 있지만 일단 시도해봄

# 그룹화 후 y값 합산 (x축 기준 그룹)
grouped = df.groupby(x_col)[y_col].sum().reset_index()

# 막대그래프 그리기
fig = px.bar(grouped, x=x_col, y=y_col, title=f"{x_col}별 {y_col} 합계")

st.plotly_chart(fig)
