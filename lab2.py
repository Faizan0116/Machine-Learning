# Q2
import pandas as pd
data = {
    'location':['US','India','Brazil','Russia','UK','France','Spain','Italy','Turkey','Germany'],
    'Cases':[28833039,11079979,10517232,4246079,4170519,3736016,3188553,2907825,2693164,2444169],
    'Deaths':[517204,156938,254263,86122,122705,86332,69142,97507,28502,70601],
    'Recovered':['',10763451,9386440,3811797,'', '', '', 2398352, 2565723, 2242767],
}
print(pd.Series(data))
print(pd.DataFrame(data))

# Q3
columns = ['location','Cases','Deaths','Recovered','Status']
df = pd.DataFrame(data,columns=columns)
print(df)
for x in range(len(df['Cases'])):
    if df['Cases'][x] < 3000000:
        df['Status'][x] = 'Low'
    elif df['Cases'][x] >= 3000000 and df['Cases'][x] < 4000000:
        df['Status'][x] = 'Medium'
    else:
        df['Status'][x] = 'High'

print(df)

# Q4
