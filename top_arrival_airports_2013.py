import streamlit as st
import pandas as pd

st.title('Top arrival airports in 2013')
st.subheader('This web service will allow you to get the top arrival airports in terms of passengers in 2013 on a JSON format')
st.markdown('Please insert the number of TOP airports you want to get. For instance, for the TOP 10 airports you will have to specify 10.')

try:

    n = int(st.text_input("Insert a number:"))

    pax_per_airport_2013 = pd.read_csv('https://github.com/Laurajmoreno/DS_Challenge/blob/main/pax_per_airport_2013_sorted.csv?raw=true',sep='^')
    top_airports = pax_per_airport_2013.reset_index().groupby('arr_port')['pax'].sum().sort_values(ascending=False).head(n)

    result_json = top_airports.to_json()
    st.json(result_json)

except ValueError:
    st.error('Only numbers allowed as input')
