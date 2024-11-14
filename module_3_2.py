def test_mail(email):
    test_mail_str = '@'
    test_mail_end_str = ['.com', '.ru', '.net']
    result = True

    if test_mail_str in email:
        result = False

    for i in range(len(test_mail_end_str)):
        if email.endswith(test_mail_end_str[i]):
            result = False
            break
        else:
            result = True

    return result

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if (test_mail(recipient) or test_mail(sender)):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')