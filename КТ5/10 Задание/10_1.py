# -*- coding: utf-8 -*-

import json
file = open('input 10.1.json', 'r')
arr = json.load(file)
file.close()
n = int(len(arr) ** 0.5)
m = (1 + n) * n / 2
table = [[None for j in range(n)] for i in range(n)]
j, counter = 0, 0
for i in range(n):
  k = 0
  while(k < j):
    table[i][k] = table[k][i]
    k += 1
  while(k < n):
    table[i][k] = arr[counter]
    k += 1
    counter += 1
  j += 1
file = open('output.json', 'w')
json.dump(arr, file)
file.close()
print(table)
