#Create a function called win_percentage() that takes two parameters named wins and losses.

#This function should return out the total percentage of games won by a team based on these two numbers.

# Write your win_percentage function here:
def win_percentage(wins, losses):
    return (wins / (wins + losses)) * 100

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100