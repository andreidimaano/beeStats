import pandas as pd
import matplotlib.pyplot as plot

bm = pd.read_csv('bm.csv')

a = {};

for index, row in bm.iterrows():
    if a.get(row["Bee Number"]):
        if row["What did the wings look like?"] == "Normal wings":
            a[row["Bee Number"]]["normal"] += 1
        elif row["What did the wings look like?"] == "Deformed wings":
            a[row["Bee Number"]]["deformed"] += 1
    else:
        if row["What did the wings look like?"] == "Normal wings":
            a[row["Bee Number"]] = {"normal": 1, "deformed": 0}
        elif row["What did the wings look like?"] == "Deformed wings":
            a[row["Bee Number"]] = {"normal": 0, "deformed": 1}
    # print(row["Bee Number"], row["What did the wings look like?"])

wing = {}
for key in a:
    wingtype = "normal" if (a[key]["deformed"] == 0) else "deformed"
    wing[key] = wingtype

# print(wing)

df = pd.read_csv('LineageDMV.csv')

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
        if row['Lineage'] == 'European' and wing.get(row['Bee Number']) == "normal":
            euroCount += 1
        if row['Lineage'] == 'African' and wing.get(row['Bee Number']) == "normal":
            africanCount += 1
    # print(row['Lineage'], row ['Does the bee have DWV?'])

print("acount: ", aCount, "DWV", africanCount, "percentage: ", africanCount / aCount)
print("ecount: ", eCount, "DWV", euroCount, "percentage: ", euroCount / eCount)

dwv = [100 * africanCount / aCount, 100 * euroCount / eCount]
index = ['African', 'European']
data = {"Lineage" : index, "DWV Count": dwv}

df2 = pd.DataFrame(data=data)

ax = df2.plot.bar(x="Lineage", y="DWV Count", title="Percentage of Bees with DWV and No Outward Expressions", rot=0)
plot.show()





