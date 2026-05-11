import pandas as pd

data={
    "Name":['Ram','Shyam','Suman'],
    "Age":[18,20,24],
    "City":["Mumbai","Pune","Latur"]
}
df=pd.DataFrame(data)
#print(df)

#df.to_csv("Out_Put.csv",index=False)
#df.to_excel("out_put.xlsx",index=False)
#df.to_json("out_put.json",index=False)