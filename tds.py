import streamlit as st 

st.write("""
# Welcome to My First App
""")

st.header('You can input three number and check which one is greater ')
st.header('User Input Parameter ')

def user_input():
  a = st.number_input("First_num",min_value=0,max_value=100000000,step=1)
  b = st.number_input("Second_num",min_value=0,max_value=100000000,step=1)
  c = st.number_input("Third_num",min_value=0,max_value=100000000,step=1)

  data ={'First number':a,
          'Second number':b,
          'Third number'
