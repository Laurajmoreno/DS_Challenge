import streamlit as st
import pandas as pd

st.title('Top arrival airports in 2013')
st.subheader('This web service will allow you to get the top arrival airports in terms of passengers in 2013 on a JSON format')
st.markdown('Please insert the number of TOP airports you want to get. For instance, for the TOP 10 airports you will have to specify 10.')

n = int(st.text_input("Insert a number:"))

chksize = 100000
reader = pd.read_csv('/home/dsc/Data/challenge/bookings_without_duplicates.csv' , sep='^', usecols=['year','arr_port','pax'], iterator=True, chunksize=chksize)
all_chunks= []

for df in reader:
    df = df[df['year'] == 2013]
    result_chunk = df.groupby('arr_port')['pax'].sum()
    all_chunks.append(result_chunk)
    
pax_per_airport_2013 = pd.concat(all_chunks)
top_airports = pax_per_airport_2013.reset_index().groupby('arr_port')['pax'].sum().sort_values(ascending=False).head(n)
st.table(top_airports)
