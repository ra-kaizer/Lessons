name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = int(input('Введите ваш год рождения (цифрами): '))
city = input('Введите город в котором вы проживаете: ')
email = input('Введите ваш e-mail: ')
phone = input('Введите ваш телефон: ')


def profile_inf(qname, qsurname, qyear, qcity, qemail, qphone):
    print("Ваши данные: ", qsurname, qname, ", ", qyear, "г.р., из города: ", qcity, ", контакты: ", qemail, ", ",
          qphone)


profile_inf(qsurname=surname, qname=name, qyear=year, qcity=city, qemail=email, qphone=phone)
