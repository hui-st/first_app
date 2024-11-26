import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import altair as alt

# 타이틀 텍스트 출력
st.title('**Choropleth지도 시각화(시군구)**')
st.title('👶🏻🗺️') # 이모지

st.header('Matplotlib 기반')


# geoJSON 데이터 불러오기(구글 드라이브에서 )
#df = gpd.read_file("https://drive.google.com/uc?id=1CF0X0SURf2NBfmxv4Rr4A6KOdo-PSRfM")

# Matplotlib 한글 폰트 설정
#plt.rcParams['font.family'] = 'Malgun Gothic'
#plt.rcParams['axes.unicode_minus'] = False

#import matplotlib.pyplot as plt
#import streamlit as st

# figure, axes 생성
#fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Choropleth 지도 그리기

#df.plot(
 #   column='합계출산율 (가임여성 1명당 명)',
  #  ax=ax,
   # legend=True,
    #cmap='BuPu',  # 색상 맵 (Blue-Purple)
    #legend_kwds={'label': '합계출산율', 'orientation': 'horizontal'}  # 범례 제목을 '합계출산율'로 설정
#)

# 제목 추가
#ax.set_title('시군구 기준 Choropleth 지도', fontsize=15)

# Streamlit에 Matplotlib 그래프 출력
#st.pyplot(fig)

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
