"""Сумма 11 + 22 + 33 + ... + 1010 = 10405071317.

Найдите последние десять цифр суммы 11 + 22 + 33 + ... + 10001000."""

list_sum = [i**i for i in range(1,1001)]
print(str(sum(list_sum))[0:10])