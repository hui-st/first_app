import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import requests
from io import BytesIO

# 타이틀 출력
st.title('**Choropleth 지도 시각화 (시군구)**')
st.title('👶🏻🗺️')

st.header('Matplotlib 기반')

# Google Drive의 GeoJSON 파일 다운로드
@st.cache_data  # 캐싱을 통해 반복 다운로드 방지
def load_geojson_from_drive(url):
    response = requests.get(url)
    if response.status_code == 200:
        geojson = BytesIO(response.content)
        return gpd.read_file(geojson)
    else:
        st.error(f"Error loading GeoJSON file. Status code: {response.status_code}")
        return None

# Google Drive 링크에서 파일 로드
geojson_url = "https://drive.google.com/uc?id=1CF0X0SURf2NBfmxv4Rr4A6KOdo-PSRfM"
df = load_geojson_from_drive(geojson_url)

if df is not None:
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
        legend_kwds={'label': '합계출산율', 'orientation': 'horizontal'}  # 범례 제목 설정
    )

    # 제목 추가
    ax.set_title('시군구 기준 Choropleth 지도', fontsize=15)

    # Streamlit에 Matplotlib 그래프 출력
    st.pyplot(fig)
else:
    st.error("GeoJSON 데이터를 불러오지 못했습니다.")

