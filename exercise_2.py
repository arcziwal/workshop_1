nums_names = ["pierwszą", "drugą", "trzecią", "czwartą", "piątą", "szóstą"]


def data_validator(num, list_of_nums):
    try:
        int(num)
    except ValueError:
        print("Wpisane dane nie są liczbą całkowitą")
        return False
    if num in list_of_nums:
        print("Ta liczba została już wybrana")
        return False
    if not 0 < int(num) < 50:
        print("Wpisana liczba jest poza zakresem")
        return False
    return True


print("Witaj w symulatorze LOTTO")
print("Za chwilę zostaniesz poproszony o podanie sześciu liczb. Wpisz je i każdą zatwierdź naciskając enter")
user_nums = []
for number in nums_names:
    correct_data = False
    while not correct_data:
        user_num = input(f"Podaj {number} liczbę: ")
        correct_data = data_validator(user_num, user_nums)
        if correct_data:
            user_nums.append(user_num)
print(user_nums)


