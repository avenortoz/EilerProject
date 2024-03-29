'''Простое число 41 можно записать в виде суммы шести последовательных простых чисел:

41 = 2 + 3 + 5 + 7 + 11 + 13
Это - самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной сотни.

Самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной тысячи, содержит 21 слагаемое и равна 953.

Какое из простых чисел меньше одного миллиона можно записать в виде суммы наибольшего количества последовательных простых чисел?'''

from check_simple import simple_a
n = 10**6
simple = simple_a(n)
k = 0
s = 0
while n > s:
    k += 1
    s = sum(simple[:k])

res= []

for difference in range(k,1,-1):
    for i in range(len(simple)-difference+1):
        value = sum(simple[i:i+difference])
        if value in simple:
            res.append(value)
        elif value > n:
            break
    if res:
        print(max(res),difference)
        break
