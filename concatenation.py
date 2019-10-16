#marge two dataframes together
import pandas as pn

df1 = pn.DataFrame({'Day': [1,2,3,4,5,6], 'visitor': [100, 200, 300, 50, 500,100],
        'duration': [30,45,20,5,10,15], 'buying': [10, 25, 15, 5, 45, 26],
        'amount':[15000,25000, 10000, 5600, 70000, 18000]}, index = [2019, 2018, 2017, 2016, 2015, 2014])

df2 = pn.DataFrame({'Day': [1,2,3,4,5,6], 'visitor': [52, 100, 200, 150, 200,100],
        'duration': [30,45,20,5,10,15], 'buying': [12, 35, 45, 15, 35, 36],
        'amount':[25000,20000, 20000, 5000, 50000, 18000]}, index = [2013, 2012, 2011, 2010, 2009, 2008])
df1 = df1.rename(columns={'buying':'selling'})
df2 = df2.rename(columns={'buying':'selling'})
concat = pn.concat([df1, df2])
print(concat)
