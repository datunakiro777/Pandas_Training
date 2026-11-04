import pandas as pd

#data = [1, 2, 3, 4, 4, 100, 102, 50, 43]
#series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
#print(series[series >= 100])


calories = {"day1" : 2000, "day2" : 10000, "Day3" : 5000}

series = pd.Series(calories)

print(series.loc["day1"])

series.loc["day1"] += 500

