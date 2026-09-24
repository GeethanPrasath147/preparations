#Input consists of 2 integers. The first integer corresponds to the number of friends Ross has. The second integer corresponds to the number of teams.
mem=int(input())
team=int(input())

eqt=mem//team

lo=mem%team

print("The number of friends in each team is",eqt,"and left out is",lo)
