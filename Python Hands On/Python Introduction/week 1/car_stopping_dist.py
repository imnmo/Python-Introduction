#car stopping distance calculator
velocity = int(input('Enter your velocity:'))
Breakingdistance = (velocity / 10) * (velocity / 10)
Reactiondistance = (velocity / 10) * 3
Stoppingdistance = Reactiondistance + Breakingdistance
print (Breakingdistance,Reactiondistance,Stoppingdistance)
