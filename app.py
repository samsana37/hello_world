import streamlit as st
import pandas as pd
from model import train
import numpy as np

st.title("Hello World App")
st.header("Welcome to the Hello World App")

#train model
model = train()

#sidebar
st.sidebar.header("Input Features")
input_value = st.sidebar.slider(" select a value f(x)",1, 10, 1)

#prediction 
input_array = np.array([[input_value]])
prediction = model.predict(input_array)

#display prediction
st.write(f"### Input value: {input_value}")
st.write(f"### Output value: {prediction[0]:.2f}")
