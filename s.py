import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import geopandas as gpd

# 타이틀 텍스트 출력
st.title('**Choropleth지도 시각화(시군구)**')
st.title('👶🏻🗺️')

st.header('Matplotlib 기반')


# geoJSON
df = gpd.read_file("C:/Users/rlawj/data/dataframe.geojson")

# Matplotlib 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# figure, axes 생성
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Choropleth 지도 그리기
df.plot(
    column='합계출산율 (가임여성 1명당 명)',
    ax=ax,
    legend=True,
    cmap='BuPu',  # 색상 맵 (Blue-Purple)
    legend_kwds={'label': '합계출산율', 'orientation': 'horizontal'}  # 범례 제목을 '합계출산율'로 설정
)

# 제목 추가
ax.set_title('시군구 기준 Choropleth 지도', fontsize=15)

# Streamlit에 Matplotlib 그래프 출력
st.pyplot(fig)
