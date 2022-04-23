import streamlit as st
import numpy as np
import pickle
import requests
import xgboost as xgb
import sklearn


def predict_cal(data_list):
    input_data_as_numpy_array = np.asarray(data_list)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    model2 = xgb.XGBRegressor()
    model2.load_model('data.pkl')
    cal = model2.predict(input_data_reshaped)
    return cal[0]

def int_gen(gender):
    if (gender == 'Male'):
        return 0
    else:
        return 1



def run():
    st.title("Calories Calculator")
    gender_list = ['Male', 'Female']
    gender = st.selectbox('Gender', gender_list)
    age = st.text_input('Age')
    weight = st.text_input('Weight')
    height = st.text_input('Height')
    Workout_list = ['Cycling', 'Swimming', 'Running', 'Yoga', 'Strength Training']
    Workout = st.selectbox('Worktout' , Workout_list)
    heart_rate = st.text_input('Heart Rate')
    duration = st.text_input('Duration')
    body_temp = st.text_input('Body Temperature')

    if st.button('Predict'):
        data_list = []
        data_list.extend([int(int_gen(gender)), int(age), int(height), int(weight), int(duration), int(heart_rate), float(body_temp)])
        calories = predict_cal(data_list)
        st.text("Calories burnt are:" + str(calories))
run()