def square_triangle(a, b):
  return a * b * 0.5

def square_rectangle(a, b):
  return 2 * square_triangle(a, b)


a = list(map(int, input().split()))
print(square_rectangle(a[0], a[1]))