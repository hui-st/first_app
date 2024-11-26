import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import altair as alt



st.write('topojson형식을 변화시켜 데이터 크기를 줄여 깃허브에 데이터를 올리는 법을 찾아서 altair로 그려봤지만 제대로 출력되지는 않았습니다')
# Streamlit 앱 타이틀
st.title('**시군구 기준 Choropleth 지도**')
st.header('Altair 기반 시각화')

# TopoJSON 데이터 URL
topojson_url = "https://raw.githubusercontent.com/hui-st/first_app/refs/heads/main/dataframe.json"

# Altair의 topo_feature를 사용해 TopoJSON 데이터 로드
topo_feature = alt.topo_feature(topojson_url, "dataframe")  # 'layer_name'을 파일 구조에 맞게 수정

# Choropleth 지도 생성
chart = alt.Chart(topo_feature, title='시군구 기준 Choropleth 지도').mark_geoshape().encode(
    color=alt.Color('합계출산율 (가임여성 1명당 명):Q', title='합계출산율')
).project(
    type='identity',  # 좌표계가 이미 정의된 경우
    reflectY=True
).properties(
    width=800,
    height=600
)

# Streamlit에 Altair 차트 출력
st.altair_chart(chart)
