def is_year_leap(year):
    if int(year) % 4 == 0:
        return True
    else:
        return False


user_year = input("Введите год для проверки: ")
test_year = is_year_leap(user_year)
print("год " + user_year + ":", test_year)
