import random

blueBallRS = sorted(random.sample(range(1, 34), 6))
redBallRS = random.randrange(1, 17)

print(blueBallRS, ':', redBallRS)
