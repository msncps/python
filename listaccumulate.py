
import pandas as pd  

    
# List1  

lst = [['Jan', 25], ['Feb', 30], 

       ['Mar', 26], ['Apr', 22]] 

    

df = pd.DataFrame(lst, columns =['Month', 'Sales'])
TotalUptoPrevRow = 0

for row in range(len(df)): 
    TotalUptoPrevRow = TotalUptoPrevRow +  df.loc[row, "Sales"]

    df.loc[row, "Cum Sales"] = TotalUptoPrevRow
