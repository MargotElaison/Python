def month_to_season(month_num):
    month_map = {
        1: "Зима",
        2: "Зима",
        3: "Весна",
        4: "Весна",
        5: "Весна",
        6: "Лето",
        7: "Лето",
        8: "Лето",
        9: "Осень",
        10: "Осень",
        11: "Осень",
        12: "Зима",

    }
    if month_num in month_map:
        print("Месяц " + str(month_num) + ":", month_map[month_num])
    else:
        print("Такого месяца не существует!")


for i in range(1, 14):
    month_to_season(i)
