from random import choice


def password_generator():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''

    for n in range(8):
        password += choice(chars)

    return password


def send_name(name, email, password):

    return f'''Привет {name}. Ты зарегестрирован(-а) в нашей школе бровистов! 
    Твой логин: {email}, пароль: {password}'''
