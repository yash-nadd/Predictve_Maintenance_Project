import pickle
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Failure Classifier",
    page_icon = "images/icon.jpg"
)

st.title("Predictive Maintenance")
st.image("images/image.jpeg")
st.write("\n")

st.markdown(
    """
Predictive maintenance primarily focuses on detecting upcoming possible failures in the system as well as it also ensures that we will not have to run maintenance frequently. Hence, it also saves money as well as time. 
    """
)

with open ('/home/yash/Desktop/ml_projects/Predictive_Maintenance_Project/model/model.pkl','rb') as model_file:
    model = pickle.load(model_file)

col1,col2= st.columns(2)

with col1:
    air = st.number_input(label = "Air Temperature")
    process = st.number_input(label="Process Temperature")
    rpm = st.number_input(label = "Rotational Speed")

with col2:
    torque = st.number_input(label='Torque')
    tool_wear = st.number_input(label='Tool Wear')
    type = st.selectbox(label='Type', options=['Low', 'Medium', 'High'])

def prediction(air, process, rpm, torque, tool_wear, type):
    df_input = pd.DataFrame({
        'Air_temperature': [air],
        'Process_temperature': [process],
        'Rotational_speed': [rpm],
        'Torque': [torque],
        'Tool_wear': [tool_wear],
        'Type': [type]
    })
    
    prediction = model.predict(df_input)
    return prediction

if st.button('Predict'):
    predict = prediction(air, process, rpm, torque, tool_wear, type)
    st.success(predict)