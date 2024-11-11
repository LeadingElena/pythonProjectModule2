first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
cnt = 0
if first == second:
    cnt = cnt + 1
if first == third:
    cnt = cnt + 1
if second == third:
    cnt = cnt + 1

if cnt == 1:
    print(2)
elif cnt > 1:
    print(3)
else:
    print(0)