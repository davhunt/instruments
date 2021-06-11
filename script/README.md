
# Automating Script

Goal of this script is to automate the scoring process of different Surveys.

## Data Structure

The CSV file will contain rows and columns

***ROWS***: Each row composes of a different participant 

***COLUMNS***:
 - Each question(item, identified by _ix) in the instrument(questionnaire) is a column
     - Example:
     - ![image](https://user-images.githubusercontent.com/58539319/121746371-ca8bc580-cad3-11eb-86f8-dc688842ea43.png)
 - The scoring for each instrument is also a column
   - Example:
   - ![image](https://user-images.githubusercontent.com/58539319/121755731-eb5d1680-cae5-11eb-8cb4-a4069369c60e.png)

 - There are timestamps that mark the start and the end of each instrument
 
 
 
 ## Features
  - Correctly scores each different instrument's session, run and event and adds the result to a new column at the end of the respective session, run or event
       - Example:
       - ![image](https://user-images.githubusercontent.com/58539319/121755490-50643c80-cae5-11eb-869b-8ebc75969b0f.png)
       - ![image](https://user-images.githubusercontent.com/58539319/121755614-9f11d680-cae5-11eb-89e8-3ae016f24665.png)

      
