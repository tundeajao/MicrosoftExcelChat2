#After putting the python on you system at the command line of the cmd file 
# write the following subsequently
# 1.	pip install pandas
# 2.	pip install pandas_datareader
# 3.	pip install matplotlib
# 4.	pip install beautifulSoup4
# 5.	pip install sklearn


#then it is important to import the functionality to the files you have downloaded.
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#put the start and end dates in variables
start = dt.datetime(2000,1,1)
end = dt.datetime(2019,12,31)

#call the Yahoo Finance Page - put in a variable or datafeed
df = web.DataReader('TSLA', 'yahoo', start, end)

#print the lst 10 rows
print(df.head(10))

#print the last 10 rows
print(df.tail(10))

#transfer the data to a csv file.
df.to_csv('tsla.csv')

#you can read the csv file - put in the df variable
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#display.
print(df.head())