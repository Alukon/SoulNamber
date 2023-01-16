def soul(num):
    while len(str(num)) > 1:
        # пока (num)) > 1 считываем значения
        num = sum(
            [int(n)
             # преобразуем строку в цифру
             # идем по строке
             for n in list(str(num))
             # проверяем строку на цифру
             if n.isdigit()
             ]
        )
    return num
# дата
date = '24.02.2022'
s = soul(date)
print(date, '=>', s)

# # целое число
# num = 1357
# s = soul(num)
# print(num, '=>', s)
#
# # вещественное число
# pl = 3.1548897
# s = soul(pl)
# print(pl, '=>', s)



