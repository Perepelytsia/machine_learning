import math
import random
import json

data = []
for i in range(1000):
    x1 = random.randint(2, 3)
    x2 = random.randint(1, 23)
    x3 = random.randint(17, 230)
    x4 = random.randint(1, 23)
    y = math.ceil((6 * (math.exp(x1) + math.log2(x2)) + 8 * math.cos(x3)) / (x4 - math.pi))
    data.append({'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'y': y})
    
with open('data.json', 'w') as f:
    json.dump(data, f)    
