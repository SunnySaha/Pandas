import pandas as pn

dict = {'Day': [1,2,3,4,5,6], 'visitor': [100, 200, 300, 50, 500,100],
        'duration': [30,45,20,5,10,15], 'buying': [10, 25, 15, 5, 45, 26],
        'amount':[15000,25000, 10000, 5600, 70000, 18000]}

dataframe = pn.DataFrame(dict)
#print(dataframe)
#print(dataframe.head(4))
dataframe = dataframe.set_index(['Day']) #set day column as index
dataframe = dataframe.rename(columns = {'buying': 'selling'})
sd = dataframe.reindex(columns=['visitor', 'amount']) #print exactly visitor & amount
print(sd)
print(dataframe)
#print(dataframe.tail(3))