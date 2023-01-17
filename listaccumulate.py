import pandas as pd  
# List1  
lst = [['Jan', 25], ['Feb', 30], 
       ['Mar', 26], ['Apr', 22]] 
df = pd.DataFrame(lst, columns =['Month', 'Sales'])
TotalUptoPrevRow = 0 # to start with cumulative with using 0
for everyrow in range(len(df)): #for repeating every row
    TotalUptoPrevRow = TotalUptoPrevRow +  df.loc[everyrow, "Sales"] #actual formula for totalling
    df.loc[everyrow, "Cum Sales"] = TotalUptoPrevRow #for storing the total
    df

df['Cumulative Sales'] = df['Sales'].cumsum()
df
