import pickle
import streamlit as st
pickle_in=open('hdp.pkl','rb')
clf=pickle.load(pickle_in)

a = st.slider('How old are you?', 0, 130, 25)
b = st.slider('How many cigartees you smoke daily?', 0,20,1)
c = st.slider('Total Cholestrol?', 50, 250, 10)
d = st.slider('Systolic BP ?', 70, 230, 10)
e = st.slider('Diastolic BP?', 60, 120, 5)
f = st.slider('BMI?', 15,30,1)
g = st.slider('Heart Rate?', 50, 130, 5)
h = st.slider('Glucose levels?',100, 250, 15)



'''a=st.number_input('AGE')
b=st.number_input('CIGARETTES PER DAY')
c=st.number_input('TOTAL CHOLESTROL')
d=st.number_input('SYSTOLIC BP')
e=st.number_input('DISTOLIC BP')
f=st.number_input('BMI')
g=st.number_input('HEART RATE')
h=st.number_input('GLUCOSE')'''


if st.button('PREDICT'):
    result=clf.predict([[a,b,c,d,e,f,g,h]]).squeeze()
    if result==0:
        st.success('YOUR RISK IS LOW')
    else:
        st.success('YOUR RISK IS HIGH')

  
