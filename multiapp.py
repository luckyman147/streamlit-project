import streamlit as st 

class MultiApp:
    def __init__(self, ):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application
        # Parameters
        func:
            the python function to render this app
        title:
            title of the app
        """    
        self.apps.append({
            "title": title,
            "function": func

        })
    def run(self):
        #app= st.sidebar.radio
        app=st.selectbox('Navigation',self.apps,format_func=lambda apps:apps['title'])    
        
        app['function']()
