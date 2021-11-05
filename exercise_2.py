nums_names = ["pierwszą", "drugą", "trzecią", "czwartą", "piątą", "szóstą"]

print("Witaj w symulatorze LOTTO")
print("Za chwilę zostaniesz poproszony o podanie sześciu liczb. Wpisz je i każdą zatwierdź naciskając enter")
user_nums = []
for number in nums_names:
    user_num = input(f"Podaj {number} liczbę: ")
    user_nums.append(user_num)
print(user_nums)
