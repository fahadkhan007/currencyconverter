import streamlit as st
import pandas as pd
import requests
st.set_page_config(
    page_title="Currency Converter 💸",  
    page_icon="💱",                      
    layout="centered",                  
)

st.title("Currency Converter")

amnt=st.number_input("Enter the amount to be Converted: ",min_value=0)

from_currency=st.selectbox("Select the currency type of entered amount: ",["USD","INR","EUR","GBP","JPY","SAR","AED","BHD","QAR"])
to_currency=st.selectbox("Select the currency type to be converted: ",["USD","INR","EUR","GBP","JPY","SAR","AED","BHD","QAR"])

if st.button("convert"):
    params={
        "access_key": "089c31b83218fba3960fa04d8b9765cb",
        "from": from_currency,
        "to": to_currency,
        "amount": amnt,
        "format": 1
    }
    url="http://api.exchangerate.host/convert"
    response=requests.get(url,params=params)
    data=response.json()
    conv_amount=data['result']
    

    st.write(f"the conversion rate for {from_currency} to {to_currency} is {data['info']['quote']}")
    st.success(f"{amnt} {from_currency} is equal to {conv_amount:.2f} {to_currency}")
    