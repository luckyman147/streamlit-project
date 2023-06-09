import streamlit as st 
from multiapp import MultiApp
from apps import home,data,model # import your app modules here

app=MultiApp()

st.markdown("""
#Multi-page app 
This app demonstrates multi-page app using streamlit

""")
app.add_app("Home",home.app)
app.add_app("Data",data.app)
app.add_app("Model",model.app)
app.run()