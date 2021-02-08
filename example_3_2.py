def user_data(u_name, u_surname, u_birth_year, u_town, u_email, u_phone):
    """Возвращает данные о пользователе одной строкой.

    Именованные параметры:
    u_name -- имя
    u_surname -- фамилия
    u_birth_date -- год рождения
    u_town -- город проживания
    u_email -- email
    u_phone -- телефон

    """
    print(
        f'Имя: {u_name} | Фамилия: {u_surname} | Год рождения: {u_birth_year} г.р. | Город проживания: {u_town} | Email: {u_email} | Телефон: {u_phone}')


n = input('Введите имя: ')
s = input('Введите фамилию: ')
b = input('Введите год рождения: ')
t = input('Введите город проживания: ')
e = input('Введите email: ')
p = input('Введите номер телефона: ')

user_data(u_phone=p, u_email=e, u_town=t, u_birth_year=b, u_surname=s, u_name=n)
