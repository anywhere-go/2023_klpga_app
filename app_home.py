import streamlit as st

def run_app_home():
    st.subheader('환영합니다~')
    st.text('좋은 서비스로 제공하겠습니다.')
    st.text('자동 배포 처리된 앱입니다.')
    st.text('이 앱은 2023년 한국여자프로골프(KLPGA)데이터에 대한 내용입니다.')
    st.text('데이터 분석도 가능하고, 골프 기록 정보를 넣으면 상금도 예측해 줍니다.')

    img_url ="https://cdn.golifekorea.com/news/photo/202101/941_2073_3414.jpg"
    
    st.image(img_url)