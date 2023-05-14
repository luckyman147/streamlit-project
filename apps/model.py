import streamlit as st 
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def app():
    st.write('Model')

    st.write('this is the model page of multipage app')
    st.write('The model performance of iris dataset is presented below ')

    # Load iris dataset 
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    #model building 
    st.header("Model performance")
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    clf=RandomForestClassifier()
    clf.fit(X_train,Y_train)
    score=clf.score(X_test,Y_test)
    st.write("Accuracy")
    st.info(score)
    st.write("Classification report")
    st.write(classification_report(Y_test,clf.predict(X_test)))

