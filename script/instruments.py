import pandas as pd
import json


class Adexi:
    def __init__(self,columns,dataframe,jsonData):
        """
    Parameters
    ----------
    columns: list that contains the names of all the columns,
    dataframe: a pandas dataframe object that contains all the csv file info,
    jsonData: a python dictionary that contains information about each instrument
    
    Attributes
    ----------
    columns: stores the list of columns
        type: list
    df: stores the dataframe
        type: datafram
    sections: stores each section from timestamp to complete
        type: list
    nullRow: stores the rows that contain empty values for a section
        type: list
    """
        self.columns = columns
        self.df = dataframe
        self.sections = []
        self.jdata = jsonData
        self.nullRow = []
        
    def getSections(self):
        """
        Loops through each column,
        each time a column name ends with timestamp or complete
        we store the index of that column in the sections list
        """
        for index,column in enumerate(self.columns):
            split = column.split("_")
            if split[-1]=='timestamp' or split[-1]=='complete':
                self.sections.append(index)
    
    def missingData(self, position):
        """
        Selects a starting and ending index from the sections list,
        and looks through each row checking if any there is a missing value.
        If a row has a missing value, we store the index of that row in the nullRow list.
        We do this to ignore this row for calculating the score for this section.
        """
        index = self.df.index
        selected = self.df.columns[self.sections[position]+1:self.sections[position+1]]
        for i in selected:
            if len(self.df.loc[self.df[i].isnull()].index) > 0:
                if self.df.loc[self.df[i].isnull()].index[0] not in self.nullRow:
                    self.nullRow.append(self.df.loc[self.df[i].isnull()].index[0])
            
    
    def addNewColumn(self,score,name,position):
        """
        adds a new column to the dataframe at the specified "position",
        the column data will be the calculated "score"
        and the name will be the "name"
        
        Parameters
        ----------
        score: a dataframe column that contains the data to be stored in the new column
        name: the name of the column
        position: the position where the column will be inserted
        """
        self.df.insert(loc = self.sections[position+1]+1,
                  column = name+"_"+self.df.columns[self.sections[position+1]].split("_",1)[1].split("_comp")[0],
                  value=score,
                  allow_duplicates=False) 
    
    def subscore(self, columns_arr,position):
        """
        Calculates the subscore by adding the specified columns,
        it uses the indexes stored in the sections list to go through every section
        for the instrument
        
        Parameters
        ----------
        columns_arr: list of the columns to be summed
        position: position in the sections list for this instrument
        """
        df = self.df.drop(self.nullRow)
        selected = df.columns[self.sections[position]+1:self.sections[position+1]]
        selectedCols = []
        for i in columns_arr:
            selectedCols.append(selected[i-1])
        return df[selectedCols].sum(axis=1)
    
    def addNewDataColumns(self,instrument):
        """
        Adds all the columns for the instrument for each of its sections
        by looping through the sections list
        """
        i = 0
        count = 1
        while i < len(self.sections):
            if i%2 == 0:
                self.missingData(i)
                df = self.df.drop(self.nullRow)
                addition = df.iloc[:, self.sections[i]+1:self.sections[i+1]].sum(axis=1)
                self.addNewColumn(addition,list(self.jdata)[0]+'_total-score', i)
                self.addNewColumn(self.subscore(self.jdata[instrument][0][list(self.jdata[instrument][0])[0]],i),
                                  list(self.jdata[instrument][0])[0], i)
                self.addNewColumn(self.subscore(self.jdata[instrument][0][list(self.jdata[instrument][0])[1]],i),
                                  list(self.jdata[instrument][0])[1], i)
                try:
                    self.nullRow = []
                    self.sections[i+2]+=(3*count)
                    self.sections[i+3]+=(3*count)
                    count+=1
                except IndexError:
                    break;
            i+=1


