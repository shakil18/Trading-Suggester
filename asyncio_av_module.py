
import asyncio

import pandas as pd
from alpha_vantage.async_support.timeseries import TimeSeries

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']


async def get_data(symbol):
    ts = TimeSeries(key='a2eabd926cmshe4c70252db43f65p12240cjsn61e424f14829')
    data, _ = await ts.get_quote_endpoint(symbol)
    await ts.close()
    return data


loop = asyncio.get_event_loop()
tasks = [get_data(symbol) for symbol in symbols]
group1 = asyncio.gather(*tasks)
results = loop.run_until_complete(group1)
loop.close()

dict_0 = dict_1 = dict_2 = dict_3 = {}

for i in range(5):
    if i == 0:
        dict_0 = results[i]
    elif i == 1:
        dict_1 = results[i]
    elif i == 2:
        dict_2 = results[i]
    elif i == 3:
        dict_3 = results[i]

data1 = pd.DataFrame(dict_0, index=[0])
data1 = data1.rename(columns={'01. symbol': 'Symbol',
                              '02. open': 'Open',
                              '03. high': 'High',
                              '04. low': 'Low',
                              '05. price': 'Price',
                              '06. volume': 'Volume',
                              '07. latest trading day': 'Latest Trading Day',
                              '08. previous close': 'Previous Close',
                              '09. change': 'Change'})

data2 = pd.DataFrame(dict_1, index=[0])
data2 = data2.rename(columns={'01. symbol': 'Symbol',
                              '02. open': 'Open',
                              '03. high': 'High',
                              '04. low': 'Low',
                              '05. price': 'Price',
                              '06. volume': 'Volume',
                              '07. latest trading day': 'Latest Trading Day',
                              '08. previous close': 'Previous Close',
                              '09. change': 'Change'})
data3 = pd.DataFrame(dict_2, index=[0])
data3 = data3.rename(columns={'01. symbol': 'Symbol',
                              '02. open': 'Open',
                              '03. high': 'High',
                              '04. low': 'Low',
                              '05. price': 'Price',
                              '06. volume': 'Volume',
                              '07. latest trading day': 'Latest Trading Day',
                              '08. previous close': 'Previous Close',
                              '09. change': 'Change'})
data4 = pd.DataFrame(dict_3, index=[0])
data4 = data4.rename(columns={'01. symbol': 'Symbol',
                              '02. open': 'Open',
                              '03. high': 'High',
                              '04. low': 'Low',
                              '05. price': 'Price',
                              '06. volume': 'Volume',
                              '07. latest trading day': 'Latest Trading Day',
                              '08. previous close': 'Previous Close',
                              '09. change': 'Change'})

pd.options.display.width = None

print(data1, '\n')
print(data2, '\n')
print(data3, '\n')
print(data4, '\n')
