from alpha_vantage.timeseries import TimeSeries
import specific_date_months as spd

key = 'a2eabd926cmshe4c70252db43f65p12240cjsn61e424f14829'
ts = TimeSeries(key)

symbol_data, meta_data = ts.get_daily(symbol='AAPL')
for index, value in enumerate(spd.series_monday):
    print(symbol_data[value])


