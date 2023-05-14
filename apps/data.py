import streamlit as st 
import numpy as np 
import pandas as pd
from sklearn import datasets

def app():
    st.title('Data')
    
    st.write('this is the **data** page of the multi page app')
    st.write('The following is the dataframe of the **iris** dataset')

    iris=datasets.load_iris()
    X=pd.DataFrame(iris.data,columns=iris.feature_names)
    Y=pd.Series(iris.target,name='class')
    df=pd.concat([X,Y],axis=1)
    df['class']=df['class'].map({0:"setosa",1:"versicolor",2:"virginica"})
    st.write(df)

    