#In addition to standard division using '/' in python you can also use '%' to get modulo or remainder division 

----- #Leftover Calculator ----- 
#Think of % as the leftover calcualtor if you shared everything evenly 

#If you have an 8 slice pizza and 3 friends 
leftovers = 8 % 3 
print(leftovers) 
#[output] 2 

----- #Team Assignment ---- 
#You are the 27th person in line. Everyone in line is counted off by 4s to determine which team they are on. 

#Your team number would be remainder 
my_team = 27 % 4
print("My team number is:", my_team)
#[output] My team number is: 3 

#Calculate the team numbers for those around you in line 
front_team2 = 25 % 4 
front_team = 26 % 4 
behind_team = 28 % 4 
behind_team2 = 29 % 4 
print(front_team2, front_team, my_team, behind_team, behind_team2)
#[output] 1 2 3 0 1

#notice that team numbers are 0 through 3. There is not a team 4 because 4 divided by 4 is 0. 
