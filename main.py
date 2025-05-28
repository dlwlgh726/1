import streamlit as st
import pandas as pd
import plotly.express as px

# 구글 드라이브 직접 다운로드 링크
data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

st.title("구글 드라이브 데이터 Plotly 시각화")

# 데이터 로드
df = load_data(data_url)

st.write("### 데이터 미리보기")
st.dataframe(df.head())

# 시각화: 예를 들어 컬럼이 2개 이상일 때 scatter plot
if len(df.columns) >= 2:
    x_col = st.selectbox("X축 선택", df.columns)
    y_col = st.selectbox("Y축 선택", df.columns, index=1)
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col} Scatter Plot")
    st.plotly_chart(fig)
else:
    st.write("데이터 컬럼이 2개 이상이어야 시각화할 수 있습니다.")

