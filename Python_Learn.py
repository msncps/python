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
dataset['Calories'] = round(dataset['Calories'], 0) #- we rounded the value
dataset.head(100)
#--
dataset['Calories'].fillna(0,inplace=True) #fillna("No College", inplace = True) #-null replace with 0
dataset.head(100)
#--
dataset['Calories']=dataset.astype({'Calories':'int64'}) #-we convertig them to int
dataset.head(100)
#--creating different TBL called TBL True for NaN values
TBL = pd.isnull(dataset['Calories'])
dataset[TBL]
TBL = pd.notnull(dataset['Calories'])
dataset[TBL]
dataset
dataset = dataset.dropna(axis = 0, how ='any')
dataset
#dataset[TBL]
#dataset
#dataset = dataset.dropna(axis = 0, how ='any')
#dataset

dataset2 = pd.read_csv('data2.csv')

dataset2 = dataset2.interpolate(method ='linear', limit_direction ='forward')
#---------------------
#---------------------
dataset2 = dataset2.interpolate(method ='linear', limit_direction ='backward')
dataset2
dataset
