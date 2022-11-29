a = int(input())
s = ""
while a != 0:
  s += str(a % 8)
  a //= 8

while len(s) < 10:
  s += '0'

p = [s[i] for i in range(len(s)-1, -1, -1)]
print(p)