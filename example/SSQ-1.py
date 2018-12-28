import random

blueBallRS = []
blueBalls, redBalls = range(1, 34), range(1, 17)

for i in range(6):
    choice = random.choice(blueBalls)
    blueBallRS.append(choice)
    blueBalls.remove(choice)

blueBallRS.sort()
redBallRS = random.choice(redBalls)

print (blueBallRS), ':', (redBallRS)
