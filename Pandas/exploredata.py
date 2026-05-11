import pandas as pd
df = pd.read_csv(r"C:\Users\hp\source\repos\Python\formula1_Databricks_project\Pandas\Data.csv")
#df= pd.read_json(r"C:\Users\hp\source\repos\Python\formula1_Databricks_project\Pandas\currencies.json")
#print(df)

#print(df.head(10))# Top 10 rows
#print(df.head()) # top 5 rows
#print(df.tail(10))# last 10 rows
#print(df.tail()) # last 5 rows

#info() 
# is a method which provides
# 1- number of rows and columns
# 2- column names
# 3 - data types
# 4- non null count
# 5- data frame used memory
#print(df.info())

#describe method

#print(df.describe())
# it gives count, std, min 25%, 50%,75% and max values of numeric columns

"""
1- how big is your dataset
2- what are the names of column
shape and columns
"""
#print(f'shape:{df.shape}')# return number of rows and number of columns
#print(f'Column name:{df.columns}') # it return names of column in tuple format so we get to know which are columns

"""
1- select specific column-use square brackets
    - it will return a series( a single column)
    - it will retirn dataframe( when you select multiple columns)
    column= df["column name"]- to select single column
    subset= df["column1","column2","column3",....]
2- filter rows- use boolen conditions 
    - filterring row with specific condition - boolen indexing
    #based on single condition
    filtered_row = df[df["salary"] > 50000]  
   
3- combine multiple conditions
 #based on multiple condition
 filterrows= df[(df["salary"]>50000) & (df["salary"] < 80000)]
"""
#print(df["Order Date"])

#subset= df[['Order Date','Product Name', 'Sales']]
#print(subset)

#rowfilter = df[df['Sales']> 10]
#print(rowfilter)

#filert on multiple condition

#df2= df[(df['Sales']< 10) & (df['Sub-Category'] =='Phones')] # 
#print(df2)

#df2= df[(df['Sales']< 10) | (df['Sub-Category'] =='Phones')] # | or condition

#print(df2)
'''
print(df["Sales"].sum())
print(df["Sales"].mean())
print(df["Sales"].mean())
print(df["Sales"].min())
print(df["Sales"].count())
print(df["Sales"].agg(["sum", "mean", "max", "min"]))
'''
#print(df.info())
#print(df.groupby(["Product Name", "Sub-Category"])["Sales"].sum())
#df2= df.groupby(["Product Name", "Sub-Category"])["Sales"].sum()
df2 = df.groupby(["Product Name", "Sub-Category"], as_index=False)["Sales"].sum()

df2["Rank"] = df2["Sales"].rank(ascending=False)

print(df2.to_string(index=False))

