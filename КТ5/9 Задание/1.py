n = int(input())
m = (1 + n) * n / 2
arr = list(map(int, input().split()))
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

print(table)