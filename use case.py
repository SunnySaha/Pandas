import pandas as p
from matplotlib import style
import matplotlib.pyplot as pyplot

style.use('fivethirtyeight')

dataframe = p.DataFrame({'date': [1,2,3,4,5,6], 'visitor': [100, 200, 300, 50, 500,100],
        'duration': [30,45,20,5,10,15], 'buying': [10, 25, 15, 5, 45, 26],
        'amount':[15000,25000, 10000, 5600, 70000, 18000]}, index = [2019, 2018, 2017, 2016, 2015, 2014])
dataframe = dataframe.set_index(['date'])
sd = dataframe.reindex(columns = ['visitor', 'buying'])

db = sd.diff(axis=1)
db.plot(kind = 'bar')
pyplot.show()



