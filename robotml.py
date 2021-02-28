import streamlit as st
#import plotly_express as px
import pandas as pd

#title of the app
st.title("Robotic Process Automation DEMO")

#Add a sidebar
st.sidebar.subheader("Visualization Settings")

#setup file upload
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel File.", type=['csv','xlsx'])

global df
if uploaded_file is not None:
	print(uploaded_file)
	print("hello")

	try:
		df = pd.read_csv(uploaded_file)
	except	Exception as e:
		print(e)
		df = pd.read_excel(uploaded_file)

try:
	st.write(df)
	col= list(df.columns.values)
	#col= list(df.select_dtypes.('number').columns)
	option = st.sidebar.selectbox("Choose a field",(col))	
	#st.header(option)
	#st.write(df.isnull().sum())
	st.write(df[col].corr())
except	Exception as e:
	print(e)
	st.write("Please upload file to the application.")
	