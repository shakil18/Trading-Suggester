import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

import specific_date_months as spd

yf.pdr_override()  # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("ES=F", start="2020-06-01", end="2020-08-05")

specific_day = spd.series_monday
dfs = []
for index, value in enumerate(specific_day):
    dfs.append(data.loc[data.axes[0].date == value])

results = pd.concat(dfs, ignore_index=False)
print(results)

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
