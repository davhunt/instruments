import pandas as pd
import json
import instruments

file = pd.read_csv("/Users/osman/OneDrive/Documents/expected_input.csv",index_col="participant")
dataframe = pd.DataFrame(file)

with open('data.json','r') as infile:
    data = json.load(infile)

for instrument in data:
    if instrument == 'adexi':
        adexi = instruments.Adexi(dataframe.columns,dataframe,data,instrument)
        adexi.getSections()
        adexi.addNewDataColumns()

'''
Stores the completed document with the calculated scores
Path must be specified

Great documentation in https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

path formats allowed: Example: C:\\Users\\user\\Documents\\instrumenrs_output.csv
                                C:/Users/user/Documents/instruments_output.csv
'''
dataframe.to_csv(path_or_buf="C:\\Users\\user\\Documents\\instrumenrs_output.csv" , na_rep='NaN')