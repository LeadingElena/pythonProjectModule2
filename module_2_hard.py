number = int(input('Введите число: '))
result = []
result_test = []
if 3 <= number <= 20:
    for i in range (1, number):
        for j in range (1, number):
            if number % (i + j) == 0:
                list_test = [j, i]
                if i == j:
                    continue
                elif i != j:
                    if len(result) < 1:
                        result_test.append([i, j])
                        result.append(i)
                        result.append(j)
                    elif list_test in result_test:
                        continue
                    else:
                        result_test.append([i, j])
                        result.append(i)
                        result.append(j)

    print(number, ' - ', *result, sep = '')
else:
    print("Некорректное число")