import streamlit as st 
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

##Page extends to full width
st.set_page_config(page_title='The Machine Learning app ',layout="wide")

#model building 

def build_model(df):
    X=df.iloc[:,:-1]
    Y=df.iloc[:,-1]
    st.markdown('**1.2 Data split**')
    st.write("Training Set")
    st.info(X.shape)
    st.write("Test Set")
    st.info(Y.shape)
    st.markdown('**1.3 Variable details**')
    st.write('X variable')
    st.info(list(X.columns))
    st.write('Y variable')
    st.info(Y.name)
    #data spliting 
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=split_size)
    rf=RandomForestClassifier(n_estimators=parameter_n_estimator,
                              random_state=parameter_random_state,
                              max_features=parameter_max_feature,
                              criterion=parameter_criterion,
                              min_samples_split=parameter_min_sample_split,
                              min_samples_leaf=parameter_min_sample_leaf,
                              bootstrap=parameter_bootstrap,
                              n_jobs=parameter_n_jobs,
                              )
    rf.fit(X_train,Y_train)
    st.subheader('2. Model Performance')
    st.markdown('**2.1 Training set**')
    Y_pred_train=rf.predict(X_train)
    st.write('Coefficient of determination ($R^2$):')
    st.info(r2_score(Y_train,Y_pred_train))
    st.write('Error (MSE or MAE):')
    st.info(mean_squared_error(Y_train,Y_pred_train))
    st.markdown('**2.2 Test set**')
    Y_pred_test=rf.predict(X_test)
    st.write('Coefficient of determination ($R^2$):')
    st.info(r2_score(Y_test,Y_pred_test))
    st.write('Error (MSE or MAE):')
    st.info(mean_squared_error(Y_test,Y_pred_test))
    st.subheader("3.Model Parameters")
    st.write(rf.get_params())

st.write("""
The Machine learning app with Random Forest Regressor""")

with st.sidebar.header("2? Upload your CSV data"):
    uploaded_file=st.sidebar.file_uploader("Upload your input CSV file",type=["csv"])
    

with st.sidebar.header('2.1 Set Parameters'):
    split_size=st.sidebar.slider('Data split ratio (% for Training Set)',10,90,80,5)
    parameter_n_estimator=st.sidebar.slider('Number of estimators (n_estimators)',0,1000,100,100)
    parameter_max_feature=st.sidebar.select_slider('Max features (max_features)',options=["auto","sqrt","log2"])
    parameter_min_sample_split=st.sidebar.slider('Minimum number of samples required to split an internal node (min_samples_split)',1,10,2,1)
    parameter_min_sample_leaf=st.sidebar.slider('Minimum number of samples required to be at a leaf node (min_samples_leaf)',1,10,2,1)
with st.sidebar.header('2.2 General Parameters'):

    parameter_bootstrap=st.sidebar.select_slider('Bootstrap samples when building trees (bootstrap)',options=[True,False])
    parameter_criterion=st.sidebar.select_slider('Function to measure the quality of a split (criterion)',options=['gini',"entropy","log_loss"])
    parameter_random_state=st.sidebar.slider('Seed number (random_state)',0,1000,42,1)
    parameter_n_jobs=st.sidebar.select_slider('Number of jobs to run in parallel (n_jobs)',options=[1,-1])
    

#main panel 
#display the dataset 
st.subheader('1. Dataset')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.markdown('**1.1 Glimpse of dataset**')
    st.write(df)
    build_model(df)
else:
    st.info('Awaiting for CSV file to be uploaded')
    if st.button('Press to use Example Dataset'):
        #diabetes dataset
        #diabetes=datasets.load_diabetes()
        #X=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
        #Y=pd.Series(diabetes.target,name='response')
        #df=pd.concat([X,Y],axis=1)
        #st.markdown('The Diabetes dataset is used as the example.')
        #st.write(df.head(5))
        #build_model(df)
        #boston housing dataset
        
        #iris dataset
        iris=datasets.load_iris()
        X=pd.DataFrame(iris.data,columns=iris.feature_names)
        Y=pd.Series(iris.target,name='response')
        df=pd.concat([X,Y],axis=1)
        st.markdown('The Iris dataset is used as the example.')
        st.write(df.head(5))
        build_model(df)
        #wine dataset
        #wine=datasets.load_wine()
        #X=pd.DataFrame(wine.data,columns=wine.feature_names)
        #Y=pd.Series(wine.target,name='response')
        #df=pd.concat([X,Y],axis=1)
        #st.markdown('The Wine dataset is used as the example.')
        #st.write(df.head(5))
        #build_model(df)
        #breast cancer dataset
        #breast_cancer=datasets.load_breast_cancer()
        #X=pd.DataFrame(breast_cancer.data,columns=breast_cancer.feature_names)
        #Y=pd.Series(breast_cancer.target,name='response')
        #df=pd.concat([X,Y],axis=1)
        #st.markdown('The Breast cancer dataset is used as the example.')
        #st.write(df.head(5))
        #build_model(df)
        #heart disease dataset
        #heart_disease=datasets.load_heart_disease()
        #X=pd.DataFrame(heart_disease.data,columns=heart_disease.feature_names




