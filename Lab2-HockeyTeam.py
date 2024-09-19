# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

#team = ["Halifax Harpooners"]

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Welcome Users to the program
    print("Welcome to the Hockey Team Application!")
    #Get the user to input the name of the team they want to check
    teamName = input("Just enter the name of the team you'd like to see to get started: ")
    #Input the amount of wins the team has
    wins = input("How many wins do the {0} have? ".format(teamName))
    #Input the amount of losse the team has
    losses = input("How many losses do the {0} have? ".format(teamName))
    #Calculate the total amount of games played based on wins and losses
    totalGames = int(wins )+ int(losses) #<--Interesting note, I had to debug to get this right. I initially had int(wins + losses) but that concatenated two strings and then get the int of that which is not what I wanted 
    #Show the user all the information, how many wins, how many losses the team has and what their win/loss ratio is
    print("The {0} have {1} win(s) and {2} loss(es), with a win percentage of ".format(teamName,wins,losses) + str(round(int(wins) / totalGames,4)))







    # YOUR CODE ENDS HERE

main()