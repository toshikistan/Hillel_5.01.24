'''
додатково:

- Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля – від 8 до 16 символів)
'''
import re

password_check = ['qwe123', 'Qwerty123', 'trewQ321#',
                  'qwerety', 'qwerty@ewrq23T4qweS', 'qweaSD@f12#2$']
for password in password_check:
    if re.match(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=]).{8,16}$", password):
        print(f"Password {password} is correct")
    else:
        print(f"Password {password} is incorrect")
