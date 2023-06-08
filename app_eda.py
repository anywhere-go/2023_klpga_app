import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/20230531_klpga.csv',encoding='cp949')#한글 처리 encoding='cp949'encoding ='ISO-8859-1'

    print(df)


    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe()) #df.describe() 불러오기

    st.subheader('최대 / 최소 기록 데이터 확인하기')

    column = st.selectbox('컬럼을 선택하세요.', df.columns[4:-3]) # 4번째 컬럼 age부터 끝에서 3번째까지 슬라이싱
    st.text('최대기록 데이터')
    st.dataframe(df.loc[df[column] == df[column].max(),]) #"Age"->column 변수로 바꿈
    st.text('최소기록 데이터')
    st.dataframe(df.loc[df[column] == df[column].min(),]) #최소값
    
    st.subheader('관심 선수 검색')
    name = st.text_input('이름을 입력하세요: ')
    # st.table(df.loc[df['Player'].str.contains(name)])
    st.dataframe(df.loc[df['Player'].str.contains(name)])

    # st.subheader('관심 혈액형 검색')
    # type = st.text_input('혈액형을 입력하세요: ')
    # result = (df.loc[df['Bloodtype'] == type])
    # st.table(result) #table no good

    # st.dataframe(df.loc[df['Bloodtype'].str.contains(type)]) 
    
    
    #유저 컬럼선택 빈 선택
    st.subheader('컬럼 별 히스토그램')
    column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', df.columns[4:-3])
    bins = st.number_input('빈의 갯수를 입력하세요.', 10, 30, 20) #기본 20개 10개부터 30개

    fig = plt.figure()
    df[column].hist(bins =bins)
    # plt.show() #주피터에서만 사용

    plt.title(column +' Histogram')
    plt.xlabel(column)
    plt.ylabel('count')

    st.pyplot(fig)

    st.subheader('상관 관계 분석')
    # column_list = st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.', ('나이', '평균 타수', 'O형','AB형'))
    column_list = st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.', df.columns[4:-3])
    print(column_list)
    
    # df[column_list].corr()  #원하는 컬럼리스트 상관관계 df[['Age','gender']]
    if len(column_list) >= 2:    #유저가 2개이상 입력했을 때 그림그리기 
        fig2 = plt.figure()
        sns.heatmap(data= df[column_list].corr() , 
                annot=True, vmin=-1, vmax=1, cmap='coolwarm',
                fmt='.2f', linewidths =0.5)
        st.pyplot(fig2)

    st.subheader('혈액형 분석')

    # ratio = [41, 29, 31, 20]
    # labels = ['A', 'B','O','AB']

    # st.pyplot.(ratio, labels=labels, autopct='%.1f%%')
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    st.text('2023년 한국여자프로골프선수 혈액형 분포')
    labels = 'A', 'B', 'O', 'AB'
    sizes = [41, 29, 31, 20]
    explode = (0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'AB형')

    fig3, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig3)

    st.text('2020년 대한적십자사 혈액형별 헌혈통계')
    labels = 'A', 'B', 'O', 'AB'
    sizes = [34.1, 26.5, 27.9, 11.5]
    explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'A형')

    fig4, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig4)

    st.subheader('혈액형별 우승 경험자')
    option = st.selectbox(
    '혈액형을 선택하세요: ',
    ('A형', 'B형', 'O형','AB형'))

    # st.write('You selected:', option)
    # choice = st.selectbox('A', 'B', 'O','AB')
    if option =='A형':
        st.dataframe(df[ (df['Bloodtype'] == 'A') & (df['Total_Win'] >=1)]) #A형이면서 우승경험자
    elif option =='B형':
        st.dataframe(df[ (df['Bloodtype'] == 'B') & (df['Total_Win'] >=1)])
    elif option =='O형':
        st.dataframe(df[ (df['Bloodtype'] == 'O') & (df['Total_Win'] >=1)])
    else:
        st.dataframe(df[ (df['Bloodtype'] == 'AB') & (df['Total_Win'] >=1)])
