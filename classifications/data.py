import matplotlib.pyplot as plt
import math
import random
import json

data   = []
for i in range(500):
    x1 = random.randint(0, 100)
    x2 = random.randint(0, 100)
    if (40 * math.sin(x1 / 4) + 50) < x2:
        y = 1
    else:
        y = 0
    data.append({'x1': x1, 'x2': x2, 'y': y})

with open('train.json', 'w') as f:
    json.dump(data, f)    

data   = []
for i in range(500):
    x1 = random.randint(0, 100)
    x2 = random.randint(0, 100)
    data.append({'x1': x1, 'x2': x2})

limit  = []
for i in range(101):
    limit.append({'x1': i, 'x2': 40 * math.sin(i / 4) + 50})

with open('test.json', 'w') as f:
    json.dump(data, f)

with open('limit.json', 'w') as f:
    json.dump(limit, f)
