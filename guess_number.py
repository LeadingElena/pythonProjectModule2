import tkinter as tk
import random

num_random = random.randint(1, 100)

#cnt_attempts = 0
list_number = []
def check_number():

    value_more = 'Я загадал число больше введенного'
    value_less = 'Я загадал число меньше введенного'
    value_win = 'УРА! ПОБЕДА!'
    result_entry.delete(0, 'end')
    list_number_user.delete(0, 'end')
    #counter_attempts.delete(0, 'end')
    num1 = num_random
    num2 = int(number_entry.get())
    if num1 > num2:
        result_entry.insert(0, value_more)
    elif num1 < num2:
        result_entry.insert(0, value_less)
    else:
        result_entry.insert(0, value_win)
    list_number.append(int(num2))
    number_entry.delete(0, 'end')
    list_number_user.insert(0, list_number)

window = tk.Tk()
window.title('Угадай число')
window.geometry('350x500')
window.resizable(False, False)

number_label = tk.Label(window, text='Введите число от 1 до 100:', font=('Arial 12 normal italic'))
number_label.place(x=65, y=50)
number_entry = tk.Entry(window, width=37)
number_entry.place(x=65, y=80)

button_result = tk.Button(window, text='Проверить', width=22, font=('Arial 12 bold roman'), background="#B3E5FC",
                          command=check_number)
button_result.place(x=65, y=130)

result_label = tk.Label(window, text='Результат:', font=('Arial 12 normal italic'))
result_label.place(x=65, y=200)
result_entry = tk.Entry(window, width=37)
result_entry.place(x=65, y=230)

# counter_attempts_label = tk.Label(window, text='Счетчик попыток:', font=('Arial 12 normal italic'))
# counter_attempts_label.place(x=65, y=300)
# counter_attempts = tk.Entry(window, width=37)
# counter_attempts.place(x=65, y=330)

list_number_user_label = tk.Label(window, text='Вы вводили следующие числа:', font=('Arial 12 normal italic'))
list_number_user_label.place(x=65, y=400)
list_number_user = tk.Entry(window, width=37)
list_number_user.place(x=65, y=430)

window.mainloop()