import streamlit as st
import joblib
model = joblib.load('hpr.pkl')
st.title('House Price Prediction')
st.image('https://www.google.com/search?q=house&sca_esv=ae66a29e8f623646&udm=2&biw=1536&bih=730&sxsrf=APpeQnvh5w6MsZ-V1t5aTbZY59GUvhyCKQ%3A1787476175084&ei=z7iKatnbBKydseMPruCOmQE&oq=house&gs_lp=Egtnd3Mtd2l6LWltZyIFaG91c2UqAggAMg0QABiABBiKBRhDGLEDMggQABiABBixAzIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMggQABiABBixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIIEAAYgAQYsQMyBRAAGIAESINAULkxWLkxcAN4AJABAJgBgQGgAYEBqgEDMC4xsAEAuAEByAEA-AEBmAIEoAKWAcICBhAAGAcYHsICCBAAGAcYHhgKwgIHEAAYgAQYCpgDAOIDBBgAIF3iAwQYACBe4gMEGAAgX-IDBBgAIGDiAwQYACBh4gMEGAAgYogGAZIHAzMuMaAH1gSyBwMwLjG4B4cBwgcDMi00yAcQgAgB&sclient=gws-wiz-img#sv=CAMSURoyKhBlLTdWSFcwUWFwY3ZGTzJNMg43VkhXMFFhcGN2Rk8yTToOV1lwQ1VTQ05vUXFiWE0gBCoXCgFzEhBlLTdWSFcwUWFwY3ZGTzJNGAEwARgHIKG-0K0DSggQARgBIAEoAQ')
Area = st.number_input('SQUARE_FT')

if st.button('Predict'):
    data = [[Area]]
    prediction = model.predict(data)

    st.write('Predicted Price:', prediction[0])
