'''Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:

﻿- домашній номер телефону (тільки цифри та довжина номера)

- Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
'''


import re

home_phone_numbers = ['7260520', '232022',
                      '7740772', '25587898', '498515144', '2285']

for number in home_phone_numbers:
    if re.match(r"\d{7}$", number):
        print(f'{number} is correct!')
    else:
        print(f'{number} is incorrect!')

print('__'*10)

mobile_numbers = ['+380503620765', '+38050362076',
                  '+380676955468', '380503620769', '++380489876545']

for number in mobile_numbers:
    if re.match(r"^\+?\d{12}$", number):
        print(f'{number} is correct!')
    else:
        print(f'{number} is incorrect!')

print('__'*10)

emails = ['toshikistan@gmail.com', 'toshikistan@gmail', 'toshikistan_@gmail.com',
          'toshikistan gmail.com', 'toshikistan_gmail.com', 'toshik_istan@gmail.com']

for email in emails:
    if re.match(r"^[a-zA-Z0-9]+[._]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z]{2,}$", email):
        print(f'{email} is correct')
    else:
        print(f'{email} is incorrect')

print('__'*10)

pib_list = ['Русін Антон Сергійович', 'Айюбі Алемір Монзер Алемір Аєд', 'Борисенко Павло Володимирович', 'Гавриленко Маргарита Артемівна',
            'Захарченко Дар’я Костянтинівна', 'Мухтарова Мурват Гумаін кизи', 'Rusin Anton Sergiyovich', 'Averyanov Egor', 'Аверьянов Егор']
for pib in pib_list:
    if re.match(r"^[A-ZА-ЯЁЇІЄҐ’][a-zа-яёїієґ’]{1,19}\s[A-ZА-ЯЁЇІЄҐ’][a-zа-яёїієґ’]{1,19}\s[A-ZА-ЯЁЇІЄҐ’][a-zа-яёїієґ’]{1,19}$", pib):
        print(f'{pib} is correct')
    else:
        print(f'{pib} is incorrect')
