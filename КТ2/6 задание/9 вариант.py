"# -- coding: utf-8 --"
s = input('Введите текст: ').upper()
slov = input('Введите слово: ').upper()
sim = '.:",;-!?()'
for i in sim:
    s = s.replace(i, ' ')
s = s.split()
cnt = s.count(slov)
print(cnt)
