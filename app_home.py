import streamlit as st

def run_app_home():
    st.subheader('골프에 관심많은 분들에게~')
    st.markdown("이 앱은 :blue[한국여자프로골프선수]와 :blue[혈액형 정보]에 관심 많은 사용자를 위한 서비스입니다.")
    # st.text('이 앱은 한국여자프로골프선수와 혈액형 정보에 관심많은 사용자를 위한 서비스입니다.')
    

    img_url ="https://cdn.golifekorea.com/news/photo/202101/941_2073_3414.jpg"
    
    st.image(img_url)
    # st.text('금주의 대회일정:https://tv.naver.com/v/36687763')
    
    st.subheader('데이터 설명')
    st.markdown('2023년 5월 기준 **:green[투어 프로 선수 121명]** 기록 데이터 입니다.')
    # st.markdown('Streamlit is **_really_ cool**.')
    # st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    st.markdown(":blue[Average number of hit :평균 타수] -  참가대회 기간 타수를 평균한 값.")
    st.markdown(":blue[Average Drive :평균 드라이브거리] -  참가대회 기간 동안 티샷 드라이브 거리 평균 값.")
    st.markdown(":blue[Average Putting: 평균 퍼팅수] -  참가대회 기간 동안 퍼팅수를 평균한 값.")
    st.markdown(":blue[Green Hit Rate: 그린 적중률] -  참가대회 기간 동안 정규 타수 내에 볼을 그린에 올리는 확률.")
    st.markdown(":blue[Par Save Rate: 파 세이브율] -  참가대회 기간 동안 파온이 안 된 경우에도 파 세이브를 한 확률.")
    st.markdown(":blue[Recovery Rate: 리커버리율] -  참가대회 기간 동안 그린 적중에는 실패했지만 파 이상 기록한 확률.")
    
    st.caption('데이터 출처 2023년 5월말 기준: https://klpga.co.kr/web/record/totalRecord')