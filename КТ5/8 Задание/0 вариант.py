import math as m

def input_data() -> list:
  data = list(map(int, input().split()))
  return data

def perim(a: int,b: int,c: int) -> float:
  return (a+b+c) / 2

def S(a: int,b: int,c: int) -> float:
  p = perim(a,b,c)
  s = m.sqrt(p*(p-a)*(p-b)*(p-c))
  return s

def is_equal_s(tr_1: list, tr_2: list, tr_3: list) -> bool:  
  trs = [tr_1, tr_2, tr_3]
  squares = [S(tr[0], tr[1], tr[2]) for tr in trs]
  return len(set(squares)) == 1

tr_1 = input_data()
tr_2 = input_data()
tr_3 = input_data()

print(is_equal_s(tr_1, tr_2, tr_3))