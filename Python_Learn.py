import pandas as pd ## adding required library; pandas is one of the library used for data manipulation
dataset = pd.read_csv('data.csv') ## loading and reading data; pd is interchangeable; datasets is also is interchangeable
dataset.tail(10) # bottom 10
dataset.head(10) # top 10
dataset.head(100) # full datasets
#--
dataset.drop('Pulse',inplace = True, axis = 1) #- remove column
dataset.head(100)
#--
dataset.rename(columns = {'Date':'Entry Date'},inplace=True) #- rename column
dataset.head(100)
#--
dataset.rename(columns = {'Date':'Entry Date', 'Duration':'Time Period'},inplace=True) #- multiple column rename
dataset.head(100)
#--
dataset.dtypes #- to check the data type of column
dataset.head(100)
#--
dataset['Entry Date']=pd.to_datetime(dataset['Entry Date']) #-changing the data type of date
dataset.head(100)
dataset.dtypes #- recheck if the data type changed or not
#--
#--
#--
