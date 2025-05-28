import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import io

data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    response = requests.get(data_url)
    response.raise_for_status()  # 다운로드 실패 시 에러 발생
    file = io.StringIO(response.text)
    df = pd.read_csv(file)
    return df

st.title("구글 드라이브 데이터 Plotly 시각화")

df = load_data()

st.write("### 데이터 미리보기")
st.dataframe(df.head())

if len(df.columns) >= 2:
    x_col = st.selectbox("X축 선택", df.columns)
    y_col = st.selectbox("Y축 선택", df.columns, index=1)
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col} Scatter Plot")
    st.plotly_chart(fig)
else:
    st.write("데이터 컬럼이 2개 이상이어야 시각화할 수 있습니다.")
