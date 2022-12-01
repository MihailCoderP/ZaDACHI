# -*- coding: utf-8 -*-

import json
file = open('input 10.2.json', 'r')
arr = json.load(file)
n = len(arr)
file.close()
diag = []
trace = 0
for i in range(n):
  trace += arr[i][i]
for i in range(n):
  for j in range(n):
    if i % 2 == 0:
      arr[i][j] /= trace
file = open('output.json', 'w')
json.dump(arr, file)
file.close()
print(arr)
