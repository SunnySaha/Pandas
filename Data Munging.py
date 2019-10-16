import pandas as pd

file = pd.read_csv('parsingagain.csv')
file.to_html('prac.html')