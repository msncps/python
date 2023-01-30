# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request

#num = int(input("enter number"))
#while num <10 or num >20:
  #print("not in range enter again")
  #num = int(input("enter number"))
  
#print("number with in range thank you")

# # uploading the data-
# import pandas as pd 
# data=pd.read_csv('Sales.csv')
# data

# #number of rows imported as pd dataset-
#len(df)

# #see column title only-
#df.columns

# #number of columns
#len(df.columns)

# #top rows, remember the bracket always give top or bottom 5 unless you put the number of rows you need
#df.head(10) 

# #bottom rows always give top or bottom 5 unless you put the number of rows you need
#df.tail()

# #information on the column
#df.info()

# #get stats on the column ; like summary function
#df.describe()

# #transpose
#df.describe().transpose()

# #Renaming the columns of a dataframe
#df.columns
#df.columns = ['OrderID', 'OrderDate', 'ShipDate', 'ShipMode', 'CustomerID',
#       'CustomerName', 'City', 'PostalCode', 'ProductID', 'Category',
#       'Sub-Category', 'ProductName', 'Sales', 'Quantity', 'Discount',
#       'Profit']
#df.head()

# #three parts 
# #rows
# #columns
# #combine the two
# df
# df[20:25]
# df[:]
# df[45:] # row count 45 and below
# df[:40]
# #reverse the dataframe
# df[::-1]
# df
# #get only every 5th row
# df[::5]

#extract only one column
#df.columns
#df.head()
#df['Customer Name']
#extract two columns
#['Customer Name','City']
# df[['Customer Name','City']]
# df[['Customer Name','City']].head()
# df.City.head()
# #combining the two or multiple columnns
# df[20:25][['Customer Name','City','Product Name']]
# df[['Product Name','Category','Sales','Discount']][40:50]
# #mathematical operation multiply
# Tot_Sales = df.Sales * df.Discount
# Tot_Sales.head()
# #add column into your dataframe
# df['Total Sales'] = df.Sales * df.Discount
# df.head(10)
# #removing the column
# df.head()
# df.drop('Total Sales', 1)
# df
# df=df.drop('Total Sales', 1)
# df
# df.head()
# #filter criteria on profit < 15
# df.Profit<15
# Filter1 = df.Profit<15
# df[Filter1]
# df.Quantity > 5
# Filter2 = df.Quantity>5
# df[Filter2] #  adding filter in dataframe
# df[Filter1 & Filter2] # addig filter with multiple conditions
# #OR
# df[(df.Profit<15) & (df.Quantity >5)] # addig filter with multiple conditions - different apporach
# df.head()
# df.columns
# #rename the column name
# df.columns = ['OrderID', 'OrderDate', 'ShipDate', 'ShipMode', 'CustomerID',
# 'CustomerName', 'City', 'PostalCode', 'ProductID', 'Category',
# 'Sub-Category', 'ProductName', 'Sales', 'Quantity', 'Discount',
# 'Profit']

# df.head()

# df[df.ShipMode == "First Class"]
# #Unique category 
# df.City.unique()

# #find out about everything about 'Los Angeles'

# df[df.City == "Los Angeles"]

#.at for labels. even integers are treated as lables
#.iat for integer locations

#df.iat[3,4]
#df.iat[0,1]
#df.iat[0,1]
#df.at[8,'Customer Name'] #hm why it is skipping first row

import numpy as np
import pandas as pd
import seaborn as sns
import os
# # data = pd.read_csv('Google_Stock_Price_Train.csv')
# data

# data.head(200)

# data.tail(200)

# data.shape

# data.columns

# data.duplicated().sum() #The duplicated() method returns a Series with True and False values that describe which rows in the DataFrame are duplicated and not.

# data.isnull().sum() # returns the number of missing values in the dataset

# data.info() #The information contains the number of columns, column labels, column data types, memory usage, range index, and the number of cells in each column

# data.describe() #returns description of the data in the DataFrame. If the DataFrame contains numerical data, the description contains these information for each column: count - The number of not-empty values. mean - The average (mean) value.

# data.nunique() #returns the number of unique values for each column. By specifying the column axis ( axis='columns' ), the nunique() method searches column-wise and returns the number of unique values for each row.

# data.corr() #used to find the pairwise correlation of all columns in the Pandas Dataframe in Python. Any NaN values are automatically excluded. Any non-numeric data type or columns in the Dataframe, it is ignored.

# import matplotlib.pyplot as plt #Pyplot is a collection of functions in the popular visualization package Matplotlib. Its functions manipulate elements of a figure, such as creating a figure, creating a plotting area, plotting lines, adding plot labels, etc
# #Matplotlib is the toolkit, PyPlot is an interactive way to use Matplotlib and PyLab is the same thing as PyPlot but with some extra shortcuts. Using PyLab is discouraged now.
# import seaborn as sns #Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
# #Seaborn helps you explore and understand your data. Its plotting functions operate on dataframes and arrays containing whole datasets and internally perform the necessary semantic mapping and statistical aggregation to produce informative plots.

# import warnings #a way to warn programmers about changes in language or library features in anticipation of backwards incompatible changes coming with Python 3.0.
# warnings.filterwarnings('ignore') #  It allows you to ignore warnings from specified module.

# #to check with HM
# # f,ax=plt.subplots(figsize=(15,7))
# # sns.heatmap(data.corr(),annot=True,linewidths=0.5,linecolor="green",fmt=".4f",ax=ax)
# # plt.show()

# #to check with HM
# data_set = data.loc[:, ["Open"]].values #is a property that is used to access a group of rows and columns by label(s) or a boolean array.
# data_set

# #to check with HM
# train = data_set[:len(data_set) - 50] 
# test = data_set[len(train):]

# #to check with HM
# train.reshape(train.shape[0],1) 
# train.shape

# print(os.listdir())

df=pd.read_csv("Car.csv")
df

#handling the missing values; detecting NA values
missing_value=["N/a","na",np.nan]
df = pd.read_csv("Car.csv", na_values=missing_value)
df.isnull().sum() # empty value
df

# #to check with HM
df.isnull().any() 
sns.heatmap(df.isnull(), yticklabels=False, annot=True)
df

df11 = pd.DataFrame(data={
  "Temperature" : [1,np.nan,3,2,3],
  "Humidity" : [22,np.nan,2,np.nan,22]
})

df11

df11.dropna(how="all")

df11

df11.fillna(method='ffill')

df11

df11.fillna(method='bfill')

df11

df11.interpolate()

df11

df_dropped = df11.dropna(how="all")
df_dropped = df11.interpolate()

db = pd.read_csv('./')

# Create some sample data
# x = data['Sales']
# y = data['Quantity']

# # Create a scatter plot
# plt.scatter(x, y)

# # Add labels to the x and y axes
# plt.xlabel('x')
# plt.ylabel('y')

# # Show the plot
# plt.show()
