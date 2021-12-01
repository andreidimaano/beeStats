import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('LineageDMV.csv')

# print(df.columns)

# print(df["Does the bee have DWV?"])
s = set()

aCount = 0;
eCount = 0;
africanCount = 0;
euroCount = 0;

for index, row in df.iterrows():
    if(row['Lineage'] == 'European'):
        eCount += 1;
    elif(row['Lineage'] == 'African'):
        aCount += 1;
    if row['Bee Number'] not in s and row['Does the bee have DWV?'] == 'has DWV':
        s.add(row['Bee Number'])
        if row['Lineage'] == 'European':
            euroCount += 1
        elif row['Lineage'] == 'African':
            africanCount += 1
    # print(row['Lineage'], row ['Does the bee have DWV?'])

print("acount: ", aCount, "DWV", africanCount, "percentage: ", africanCount / aCount)
print("ecount: ", eCount, "DWV", euroCount, "percentage: ", euroCount / eCount)

dwv = [100 * africanCount / aCount, 100 * euroCount / eCount]
index = ['African', 'European']
data = {"Lineage" : index, "DWV Count": dwv}

df2 = pd.DataFrame(data=data)

ax = df2.plot.bar(x="Lineage", y="DWV Count", title="Percentage of Bees with DWV", rot=0)
plot.show()
# print(df.to_string());