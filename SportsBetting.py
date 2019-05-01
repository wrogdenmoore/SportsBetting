import pandas as pd 
#pandas to utilize excel

dbshow=pd.read_excel('database1.xlsx', 'PresentData') #bring in excel file

print(dbshow) #print the data from the present data page (print the main statistics for each team)


