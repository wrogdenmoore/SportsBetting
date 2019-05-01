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
#just concerned with the team column
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

second_team=db_inputsecond[int(usr_choice2)] #storing the number in a variable

print()
print()
print(db_inputteam[int(usr_choice1)]) #print the name of the first team selected
print()
print()
print(db[db['TEAM']==first_team]) #print the statistics for the first team
print()
print()
print()
print(db_inputsecond[int(usr_choice2)]) #print the name of the second team selected
print()
print()
print(db[db['TEAM']==second_team]) #print the statistics for the second team
print()
print()
print()
input('Press enter to continue to the statistical weight distribution') #this is to break before the next section of the weight distributions
print()
print()
print("Based on correlation between these statistics and Wins/Losses in games this year, here are the weights for each statistic:" ) #print statement as introduction
print()
print()

print(db[db['TEAM']=='Weights'])
print()

first_rating=db[db['TEAM']==first_team]['Rating'] #storing the team rating (based on the weights and statistics)


# print(first_rating[int(usr_choice1)]) #commented out--don't need to print


second_rating=db[db['TEAM']==second_team]['Rating'] #storing the second team rating

print()
print('The model uses these correlations to weight each statistic and output a recommendation')#explaining the use of the weight for the model
# print(second_rating[int(usr_choice2)])
input('Press enter to continue to the model recomendation:') #breaking one more team before the recommendation
print()
print()
print()

if first_rating[int(usr_choice1)] > second_rating[int(usr_choice2)]: #if the first rating is bigger than the second team's rating
    print("We recommend choosing the ",first_team, "based on our model.") #print the recommendation for the first team's name
else:
    print("We recommend choosing the ",second_team, "based on our model.") #print the recommendation for the second team's name

print()
print()





#OTHER NOTES AND ATTEMPTS


#Answer=pd.read_excel('database1.xlsx', 'ImplementWeights')

#db_inputanswer=Answer['Weights']

#print('Please choose a team from this list', '\n' , db_inputanswer)

#usr_choice=input('Enter the number 31 to find the weights: ')

#print(db_inputanswer[int(usr_choice)])


#2nd team 

#after second team is chosen

# db_inputsecond=db['Team']

# print('Please choose a different team from this list', '\n' , db_inputsecond)

# usr_choice=input('Enter the number next to your team of choice: ')

# print(db_inputsecond[int(usr_choice)])

# second_team=db_inputsecond[int(usr_choice)]




#Try
#CORRELATION GRAPH
#On other screen





#which is the home team?

#historical data to see which statistics are most predictive--use for weight
#regression on what combination for team 1
#regression on what combination would lead to team 2 win


#correlation:

# regdata=pd.read_excel('database1.xlsx', 'RegData')

# def plot_corr(df,size=10):
#     '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.
#     Input:
#         df: pandas DataFrame
#         size: vertical and horizontal size of the plot'''
#     corr = df.corr()
#     fig, ax = plt.subplots(figsize=(size, size))
#     ax.matshow(corr)
#     plt.xticks(range(len(corr.columns)), corr.columns);
#     plt.yticks(range(len(corr.columns)), corr.columns);

# plt.show()


#regdata['W/L']=le.fit_transform(regdata['W/L'])


#def plot_corr(df,size=10):
#'''Function plots a graphical correlation matrix for each pair of columns in the dataframe.
 #   Input:
  #      df: pandas DataFrame
   #     size: vertical and horizontal size of the plot'''
    #corr = df.corr()['W/L']
  #  plt.scatter(np.arange(len(list(df)),corr))
  #  plt.show()


#GRAPHICAL COMPONENT
    #start 
#MENTION WHERE DATA COMES FROM--VERIFY SOURCE--PROVIDE LINK
    #could include excel file
#Scraping website via beautiful soup--if have time





#Original Statistics

#db=pd.read_excel('database1.xlsx', 'Stats')
#print(db)

#db_inputteam=db['Team']

#print('Please choose a team from this list', '\n' , db_inputteam)

#usr_choice=input('Enter the number next to your team of choice: ')

#print(db_inputteam[int(usr_choice)])

#first_team=db_inputteam[int(usr_choice)]

##2nd team 

##after second team is chosen

#db_inputsecond=db['Team']

#print('Please choose a different team from this list', '\n' , db_inputsecond)

#usr_choice=input('Enter the number next to your team of choice: ')

#print(db_inputsecond[int(usr_choice)])

#second_team=db_inputsecond[int(usr_choice)]


#print(db[db['Team']==first_team])

#print(db[db['Team']==second_team])