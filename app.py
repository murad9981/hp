import streamlit as st
import joblib
model = joblib.load('hpr.pkl')
st.title('House Price Prediction')
st.image=('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJX8tOwL9Xq6gCfBLx7GO62fXroawmrPGurjwhQhR_dw&s=10')
Area = st.number_input('SQUARE_FT')

if st.button('Predict'):
    data = [[Area]]
    prediction = model.predict(data)

    st.write('Predicted Price:', prediction[0])
