import pandas as pd
import json
from instruments import adexi , aq10

with open('data.json','r') as infile:
    data = json.load(infile)

file = pd.read_csv(data["input"],index_col="record_id")
dataframe = pd.DataFrame(file)

for instrument in data:
    if instrument == 'adexi':
        adexi = adexi.Adexi(dataframe.columns,dataframe,data,instrument)
        adexi.getSections()
        adexi.addNewDataColumns()
    if instrument == 'aq-10':
        print('this gets executed')
        aq10 = aq10.AQ10(dataframe.columns,dataframe,data,instrument)
        aq10.getSections()
        aq10.addNewDataColumns()

dataframe.to_csv(path_or_buf=data["output"] , na_rep='NaN',)