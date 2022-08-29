import pickle
import streamlit as st
pickle_in=open('hdp.pkl','rb')
clf=pickle.load(pickle_in)

st.header('HEART DISEASE PREDICITON')
a = st.slider('How old are you?', 1, 130, 25)
b = st.slider('How many cigartees you smoke daily?', 0,20,10)
c = st.slider('Total Cholestrol?', 50, 250, 50)
d = st.slider('Systolic BP ?', 70, 230, 80)
e = st.slider('Diastolic BP?', 60, 120, 65)
f = st.slider('BMI?', 15,30,16)
g = st.slider('Heart Rate?', 50, 130, 55)
h = st.slider('Glucose levels?',100, 250, 105)



comment='''a=st.number_input('AGE')
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

  
