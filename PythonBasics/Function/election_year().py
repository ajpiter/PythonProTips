#A function to determine if a year will have a Presidential or Congressionial midterm elections. 
#Helpful for projecting when elections will be held years in advance 

def election_year(year): 
    if year % 4 == 0:
        return str(year) + " is a Presidential election year in the United States."
    elif year % 2 == 0: 
        return str(year) + " is a midterm election year. Voters in the U.S. will vote on House of Representatives candidates."
    else:
        return str(year) + " is not a federal election year. There might be state or local elections in various jurisdictions throughout the U.S."
        
election_year(2022) 
#[output] 2022 is a midterm election year. Voters in the U.S. will vote on House of Representatives candidates.

election_year(2065)
#[output] 2065 is not a federal election year. There might be state or local elections in various jurisdictions throughout the U.S.

election_year(2088) 
#[output] 2088 is a Presidential election year in the United States.
