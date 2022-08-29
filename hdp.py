import pickle
import streamlit as st
pickle_in=open('hdp.pkl','rb')
clf=pickle.load(pickle_in)

a = st.select_slider(
     'Select Age',
     options=[range(1,100)],
     value=(1,100))

#a=st.number_input('AGE')
b=st.number_input('CIGARETTES PER DAY')
c=st.number_input('TOTAL CHOLESTROL')
d=st.number_input('SYSTOLIC BP')
e=st.number_input('DISTOLIC BP')
f=st.number_input('BMI')
g=st.number_input('HEART RATE')
h=st.number_input('GLUCOSE')


if st.button('PREDICT'):
    result=clf.predict([[a,b,c,d,e,f,g,h]]).squeeze()
    if result==0:
        st.success('YOUR RISK IS LOW')
    else:
        st.success('YOUR RISK IS HIGH')

  
