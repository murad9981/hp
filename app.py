import streamlit as st
import joblib
model = joblib.load('hpr.pkl')
st.title('House Price Prediction')
st.image('h.jpg')
Area = st.number_input('SQUARE_FT')

if st.button('Predict'):
    data = [[Area]]
    prediction = model.predict(data)

    st.write('Predicted Price:', prediction[0])
