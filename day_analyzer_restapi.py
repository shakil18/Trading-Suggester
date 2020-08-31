import pandas as pd
import requests

import individual_days_series as spd

API_URL = "https://alpha-vantage.p.rapidapi.com/query"

# DBK.DE = Deutsche Bank

SYMBOL = "AAPL"
headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "a2eabd926cmshe4c70252db43f65p12240cjsn61e424f14829"
}

'''
    Initializing Operations 
'''
data = {"function": "TIME_SERIES_DAILY",
        "symbol": SYMBOL,
        "outputsize": "full",
        "datatype": "json"}

response = requests.request("GET", API_URL, headers=headers, params=data)
response_json = response.json()

data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient='index').sort_index(axis=1)
data = data.rename(columns={'': 'Date',
                            '1. open': 'Open',
                            '2. high': 'High',
                            '3. low': 'Low',
                            '4. close': 'Close',
                            '5. volume': 'Volume'})
'''
    specific_day: specify the series of day
'''

'''
    FOR MONDAY
'''
specific_day = spd.series_monday
dfs = []
for index, value in enumerate(specific_day):
    dfs.append(data.loc[data.axes[0].values == value])

results = pd.concat(dfs, ignore_index=False)
print(f'************************** MONDAY **************************\n'
      f'{results[["Open", "Close", "Volume", "High", "Low"]]}'
      f'\n')

# Total High/Low Counting
total_values = len(results['Open'])
count = 0
for i in range(total_values):
    if float(results['Open'][i]) - float(results['Close'][i]) < 0:
        count = count + 1

print(f'=====> Total Number of High Closed: {count}/{total_values} <=====\n')
print('======================================================================')


''' FOR TUESDAY'''
specific_day = spd.series_tuesday
dfs = []
for index, value in enumerate(specific_day):
    dfs.append(data.loc[data.axes[0].values == value])

results = pd.concat(dfs, ignore_index=False)
print(f'************************** TUESDAY **************************\n'
      f'{results[["Open", "Close", "Volume", "High", "Low"]]}'
      f'\n')

# Total High/Low Counting
total_values = len(results['Open'])
count = 0
for i in range(total_values):
    if float(results['Open'][i]) - float(results['Close'][i]) < 0:
        count = count + 1

print(f'=====> Total Number of High Closed: {count}/{total_values} <=====\n')
print('======================================================================')


''' FOR WEDNESDAY'''
specific_day = spd.series_wednesday
dfs = []
for index, value in enumerate(specific_day):
    dfs.append(data.loc[data.axes[0].values == value])

results = pd.concat(dfs, ignore_index=False)
print(f'************************* WEDNESDAY *************************\n'
      f'{results[["Open", "Close", "Volume", "High", "Low"]]}'
      f'\n')

# Total High/Low Counting
total_values = len(results['Open'])
count = 0
for i in range(total_values):
    if float(results['Open'][i]) - float(results['Close'][i]) < 0:
        count = count + 1

print(f'=====> Total Number of High Closed: {count}/{total_values} <=====\n')
print('======================================================================')


''' FOR THURSDAY'''
specific_day = spd.series_thursday
dfs = []
for index, value in enumerate(specific_day):
    dfs.append(data.loc[data.axes[0].values == value])

results = pd.concat(dfs, ignore_index=False)
print(f'***************************** THURSDAY *****************************\n'
      f'{results[["Open", "Close", "Volume", "High", "Low"]]}'
      f'\n')

# Total High/Low Counting
total_values = len(results['Open'])
count = 0
for i in range(total_values):
    if float(results['Open'][i]) - float(results['Close'][i]) < 0:
        count = count + 1

print(f'=====> Total Number of High Closed: {count}/{total_values} <=====\n')
print('======================================================================')

''' FOR FRIDAY'''
specific_day = spd.series_friday
dfs = []
for index, value in enumerate(specific_day):
    dfs.append(data.loc[data.axes[0].values == value])

results = pd.concat(dfs, ignore_index=False)
print(f'************************* FRIDAY ************************* \n'
      f'{results[["Open", "Close", "Volume", "High", "Low"]]}'
      f'\n')

# Total High/Low Counting
total_values = len(results['Open'])
count = 0
for i in range(total_values):
    if float(results['Open'][i]) - float(results['Close'][i]) < 0:
        count = count + 1

print(f'=====> Total Number of High Closed: {count}/{total_values} <=====\n')
print('======================================================================')