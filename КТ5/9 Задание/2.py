n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
diag = []
trace = 0
for i in range(n):
  trace += arr[i][i]
(arr[i][i])
for i in range(n):
  for j in range(n):
    if i % 2 == 0:
      arr[i][j] /= trace

print(arr)