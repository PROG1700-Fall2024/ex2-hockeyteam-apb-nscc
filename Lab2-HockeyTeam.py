# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

"""
Student Name:    Alex Barr
Program Title:   IT Programming
Description:     Lab 2 - Hockey Team  
"""

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

"""
So I've made some additional changes. 

I injected the win/loss ration using {n:.i} rather than concatenating a string
And as written below, I've created an additional "just for fun" program as well. 

As of completing this, I realized that I used a different naming convention for the actual project and my just for fun version.
So I've renamed some variables so that they all have the same name convention.
"""

#trying to push my knowledge of python based on my knowledge of GDscript just for fun (jff)
#Putting the teams into a list and then having a wins and losses list with each win and loss in the same numerical position in the list as the
#corressponding team
jff_team = ["Toronto Mapleleafs","Montreal Canadiens","Boston Bruins","Calgary Flames"]
jff_wins = [                   3,                   4,              2,               5]
jff_losses = [                 5,                   4,              0,               1]

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Welcome Users to the program
    print("Welcome to the Hockey Team Application!")
    #Get the user to input the name of the team they want to check
    team_name = input("Just enter the name of the team you'd like to see to get started: ")
    #Input the amount of wins the team has
    wins = input("How many wins do the {0} have? ".format(team_name))
    #Input the amount of losse the team has
    losses = input("How many losses do the {0} have? ".format(team_name))
    #Calculate the total amount of games played based on wins and losses
    total_games = int(wins )+ int(losses) #<--Interesting note, I had to debug to get this right. I initially had int(wins + losses) but that concatenated two strings and then get the int of that which is not what I wanted 
    #Show the user all the information, how many wins, how many losses the team has and what their win/loss ratio is
    win_ratio = int(wins) / total_games
    print("The {0} have {1} win(s) and {2} loss(es), with a win percentage of {3:.4}".format(team_name,wins,losses,win_ratio)) #+ str(round(int(wins) / total_games,4)))






    # YOUR CODE ENDS HERE
def jff():
    #Welcome the user to the program and tell them what it is
    print("Welcome to the Just For Fun Hockey Team Program!")
    print("In this program you can check the stats of a few hockey teams")
    print("They are absolutely accurate and totally not made up*")
    print("*this statement may or may not be true")
    #Show the teams to select
    print("Please select one of the following teams:")
    print("1 = Toronto Mapleleafs")
    print("2 = Montreal Canadiens")
    print("3 = Boston Bruins")
    print("4 = Calgary Flames")
    #Tell the user to select a team
    jff_team_number = input("Please input the corresponding number to the team you'd like to analyze: ")
    jff_team_number = int(jff_team_number) - 1

    #show the stats based on the selected team
    if jff_team_number > -1 and jff_team_number < 4: #Make sure the inputted number is between 0 and 3
        print("The {0} have {1} win(s) and {2} losses with a win/loss ratio of {3}".format(jff_team[jff_team_number], jff_wins[jff_team_number], jff_losses[jff_team_number],str(round(jff_wins[jff_team_number] / (jff_wins[jff_team_number] + jff_losses[jff_team_number]),4))))
    else:
        print("the number you selected is out of range")
    #thank the user for using the program
    print("Thanks for using the Just For Fun Hockey Team Program!")

#let the user choose which version of the program the user wants to run
which_version = int(input("Do you want to run the standard version(press 1) or the just for fun version(press 2? "))
if which_version > 0 and which_version < 3:
    if which_version == 1:
        main() #<-----------If this function eventually works like something like "Update()" in C# (using Unity), then I understand that putting the main function in an "if" statement might not be a good idea or habit to get into
    elif which_version == 2:
        jff()
else:
    print("Number is out of range. Good day.")
    
