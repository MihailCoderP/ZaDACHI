n = int(input())
sum, mult = 0, 1
arr = list(map(int, input().split()))
for i in range(n):
    if i % 2 == 0:
        sum += arr[i]
    else:
        mult *= arr[i]

print(sum, " ", mult)