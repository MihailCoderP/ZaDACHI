n = int(input())
arr = list(map(int, input().split()))
max, min, max_index, min_index = arr[0], arr[0], 0, 0
for i in range(n):
  if arr[i] > max:
    max = arr[i]
    max_index = i
  if arr[i] < min:
    min = arr[i]
    min_index = i
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(arr)