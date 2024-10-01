day = int(input("Введите день: ")) # Запрашиваем ввод числа дня.
month = int(input("Введите месяц(числом): ")) # Запрашиваем ввод числа месяца.


if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day <= 31): # Условие для определения весны: Весна: с 1 марта по 31 мая: - месяц март (3) и день >= 1, - либо любой день апреля (4), - либо любой день мая (5), - либо до конца мая (31 день).
    
    season = "Весна" # Присваиваем сезон "Весна".
    
elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 8 and day <= 31): # Условие для определения лета: Лето: с 1 июня по 31 августа: - если день >= 1 июня (6), - либо любой день июля (7), - либо любой день августа (8), - либо до конца августа (31 день).
    
    season = "Лето" # Присваиваем сезон "Лето".
    
elif (month == 9 and day >= 1) or (month == 10) or (month == 11 and day <= 30): # Условие для определения осени:  Осень: с 1 сентября по 30 ноября: - если день >= 1 сентября (9), - либо любой день октября (10), - либо до конца ноября (30 дней).
    
    season = "Осень" # Присваиваем сезон "Осень".
    
else: # Условие для зимы: Зима: с 1 декабря по 28 (или 29) февраля. Если не подошло ни одно из предыдущих условий, то оставшийся период — это зима.
    
    season = "Зима" # Присваиваем сезон "Зима".


print(f"Это: {season}") # Выводим название сезона на консоль, в соответствии с днем и месецем.