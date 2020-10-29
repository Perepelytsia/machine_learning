import math
import random
import json

data = []
for i in range(100):
    x = random.randint(-100, 100)
    y = math.ceil((math.cos(3 * x) * x + math.sin(x))/ math.pi)
    data.append({'x': x, 'y': y})

print(data)

with open('data.json', 'w') as f:
    json.dump(data, f)    
