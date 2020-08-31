from datetime import date, timedelta

''' 
    date() format: date(Year, Month, Date)
    get today's: date = date.today()
    e,g; current_date = date.today().isoformat()
'''
series_monday = [(date(2020, 8, 3) - timedelta(days=days_before)).isoformat() for days_before in range(0, 84, 7)]
series_tuesday = [(date(2020, 7, 28) - timedelta(days=days_before)).isoformat() for days_before in range(0, 84, 7)]
series_wednesday = [(date(2020, 7, 29) - timedelta(days=days_before)).isoformat() for days_before in range(0, 84, 7)]
series_thursday = [(date(2020, 7, 30) - timedelta(days=days_before)).isoformat() for days_before in range(0, 84, 7)]
series_friday = [(date(2020, 7, 31) - timedelta(days=days_before)).isoformat() for days_before in range(0, 84, 7)]

# print(f"Monday's for 3 Months: {series_monday} \n")
# print(f"Tuesday's for 3 Months: {series_tuesday} \n")
# print(f"Wednesday's for 3 Months: {series_wednesday} \n")
# print(f"Thursday's for 3 Months: {series_thursday} \n")
# print(f"Friday's for 3 Months: {series_friday} \n")

