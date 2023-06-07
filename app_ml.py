import streamlit as st
import numpy as np
import joblib
import math



def run_app_ml():
    st.subheader('기록을 입력해 보세요!')

    
    age = st.number_input('나이 입력', 18, 100)
    # st.text ('혈액형을 선택하세요!')
    # bloodtype = st.radio (options=['A형', 'B형','O형','AB형'])
    # if bloodtype == 'A형':
    #     return 1
    # elif bloodtype == 'B형':
    #     return 2
    # elif bloodtype == 'O형':
    #     return 3
    # else:
    #     return 4
        

    hit = st.number_input('평균 타수 입력', 58, 150)
    driver = st.number_input('평균 드라이브 거리 입력', 100, 400)
    putting = st.number_input('평균 퍼팅수', 18, 100)
    green = st.number_input('그린 적중률', 30, 100)
    save = st.number_input('파 세이브',50, 100 )
    recover = st.number_input('리커버리율', 30, 100)





     #버튼을 누르면 예측한 금액을 표시한다.
    if st.button('상금 예측'):
        new_data = np.array([age, hit, driver, putting, green, save, recover ])
        new_data = new_data.reshape(1,7) #1차원을 2차원으로 
  
        regressor = joblib.load('model/regressor.pkl')#파일불러오기해서 regressor저장
 
        y_pred = regressor.predict(new_data)
        print(y_pred)
   
        # st.text(y_pred)
        #28220달러짜리 차량 구매 가능합니다.
        print(y_pred[0])

        price = round(y_pred[0])

        

        print(str(price)+'원 상금 획득 가능합니다.')
        print(f'{price}원 상금 획득 가능합니다.')
        print('{}원 상금 획득 가능합니다.'.format(price))
        if price <0:
            st.error('예측이 불가능합니다.')
        else:
            st.success(f'{price}원 상금 획득이 가능합니다.')


        # st.text(f'{price}달러짜리 차량 구매 가능합니다.')
        # st.subheader(f'{price}달러짜리 차량 구매 가능합니다.')