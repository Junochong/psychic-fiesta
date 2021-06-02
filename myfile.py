import streamlit as st
import matplotlib.pyplot as plt
import requests
import numpy as np
from datetime import datetime
import json

# pretty printing of pandas dataframe

import pandas as pd

day_List=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

st.title('Cryptocurrency Live by juno')

select_time = st.sidebar.slider('Select No Of days',1,30)

st.sidebar.header('Search')

select_cu = st.sidebar.selectbox('Currency',['USD','HKD','GBP','JPY','EUR','KRW'])

select_CRP = st.sidebar.selectbox('Cryptocurrency',['BTC','ETH','DOGE','XRP','BNB','ADA','BUSD','DOT','MATIC'])

st.subheader('1 '+ select_CRP + ' For how many ' + select_cu)

# GET CURRENT PRICE DATA
def get_current_data(from_sym='BTC', to_sym='USD', exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price'    
    
    parameters = {'fsym': from_sym,
                  'tsyms': to_sym }
    
    if exchange:
        print('exchange: ', exchange)
        parameters['e'] = exchange
        
    # response comes as json
    response = requests.get(url, params=parameters)   
    data = response.json()
    
    return data


df = get_current_data(select_CRP,select_cu)
df1 = pd.DataFrame.from_dict(df, orient="index")
st.write(df1[0])



def get_current_dat(from_sym='BTC', to_sym='USD',L = '30',exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histoday'    
    
    parameters = {'fsym': from_sym,
                  'tsym': to_sym,
                  'limit':L }
    
    if exchange:
        print('exchange: ', exchange)
        parameters['e'] = exchange
        
    # response comes as json
    response = requests.get(url, params=parameters)   
    data = response.json()
    
    return data

res = get_current_dat(select_CRP,select_cu, select_time )
hist = json.dumps(res)
a = pd.DataFrame(json.loads(hist)['Data'])
a = a.set_index('time')
a.index = pd.to_datetime(a.index, unit='s')


st.write(a)

st.subheader('Pass '+ str(select_time) +' days high low open data')

st.line_chart(a[['high', 'low' ,'open']])
