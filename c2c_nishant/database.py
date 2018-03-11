import numpy as np
import pandas as pd
import csv

# Symptoms 7-8
# Dignosis 4-5

data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = []
for _ in range(100):
    val = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in np.random.choice(lst, 4):
        val[i] = 0
    ans.append(val)

print(ans[:2])
with open("clustering_dataset.csv", 'w') as f:
    a = csv.writer(f, delimiter=',')
    a.writerows(ans)
