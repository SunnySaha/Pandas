import pandas as pn

#you must join on basis of same input value

df1 = pn.DataFrame({'Day': [1,2,3,4,5,6], 'visitor': [100, 200, 300, 50, 500,100]}, index = [2019, 2018, 2017, 2016, 2015, 2020])

df2 = pn.DataFrame({'color': [1,2, 3, 4, 5, 6], 'value': [1, 5, 6, 5, 3,2 ]}, index=[2019, 2001, 2017, 2005, 2014, 2014])

join = df1.join(df2)
print(join)