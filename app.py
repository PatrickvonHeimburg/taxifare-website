import streamlit as st
import requests
import pandas as pd
import datetime



st.set_page_config(
            page_title="YOUR TAXIFARE", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="wide", # wide
            initial_sidebar_state="auto") # collapsed
st.markdown("<h1 style='text-align: center;'>YOUR TAXIFARE HERE!!</h1>", unsafe_allow_html=True)

columns = st.columns(7)
pickup_date = columns[0].date_input("Pickup Date", datetime.date.today())
pickup_time = columns[1].time_input("Pickup Time", datetime.datetime.now().time())
pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)
pickup_datetime_str = pickup_datetime.strftime("%Y-%m-%d %H:%M:%S")

#pick_up = st.text_input('pick up')
#drop_off = st.text_input('drop off')
pick_up_long=columns[2].number_input('pick up long', format="%.3f", value=-73.950655)
pick_up_lat=columns[3].number_input('pick up lat', format="%.3f", value=40.783282)
drop_off_long=columns[4].number_input('drop off long', format="%.3f", value=-73.850655)
drop_off_lat=columns[5].number_input('drop off lat', format="%.3f", value=40.783282)
passenger_count = columns[6].number_input('passengers',min_value=1, max_value=8, step=1)





url = 'https://taxifare.lewagon.ai/predict'


#if url == 'https://taxifare.lewagon.ai/predict':

    #st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


data = {
    "pickup_datetime": pickup_datetime_str,
    "pickup_longitude": pick_up_long,
    "pickup_latitude": pick_up_lat,
    "dropoff_longitude": drop_off_long,
    "dropoff_latitude": drop_off_lat,
    "passenger_count": passenger_count
}
if st.button("Get Fare Prediction"):
    response = requests.get(url, params=data)
    response.json()['fare']
    st.balloons()

map_= {
    'latitude': [pick_up_lat, drop_off_lat],
    'longitude': [pick_up_long, drop_off_long],
}
print(map_)
df=pd.DataFrame(map_)

st.map(df)
