import pandas as pd 
#pandas to utilize excel

dbshow=pd.read_excel('database1.xlsx', 'PresentData') #bring in excel file

print(dbshow) #print the data from the present data page (print the main statistics for each team)


db=pd.read_excel('database1.xlsx', 'ImplementWeights') #use implement weights sheet (holds the calculations based on the statistics)
print()
print('See above for all the NBA teams and their statistics.') #view the statistics for each team
print()
input('Press enter to continue on to team selection') #this is to break up the steps in the program and introduce the next step

db_inputteam=db['TEAM']  #first team
just concerned with the team column
print()
print('Please choose a team from this list', '\n' , db_inputteam) #list of nba teams with a number next to them
print()

usr_choice1=input('Enter the number next to your team of choice above: ') #input user choice

first_team=db_inputteam[int(usr_choice1)] #integer next to team of choice
print()
#2nd team 


db_inputsecond=db['TEAM'] #second team
print()
print('Please choose a different team from this list', '\n' , db_inputsecond) #choose a different team from the list
print()
usr_choice2=input('Enter the number next to your team of choice above: ') #put in the number
