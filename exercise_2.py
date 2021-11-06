import random

nums_names = ["pierwszą", "drugą", "trzecią", "czwartą", "piątą", "szóstą"]
nums_names_2 = ["jedną", "dwie", "trzy", "cztery", "pięć", "sześć"]
nums_names_3 = ["liczbę", "liczby"]


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
for index, value in enumerate(user_nums):
    user_nums[index] = int(value)

random_nums = []
for i in range(7):
    random_nums.append(random.randint(1, 49))
print(f"""
Zwycięskie liczby to:
{random_nums[0]}
{random_nums[1]}
{random_nums[2]}
{random_nums[3]}
{random_nums[4]}
{random_nums[5]}
""")

guessed_nums = []
for num in user_nums:
    if num in random_nums:
        guessed_nums.append(num)
if len(guessed_nums) == 1:
    print("Udało Ci się wytypować jedną liczbę. Oto ona:")
    print(guessed_nums[0])
elif len(guessed_nums) == 0:
    print("Nie udało Ci się wytypować żadnej z liczb")
else:
    print(f"Udało Ci się wytypować {nums_names_2[len(guessed_nums)-1]} liczb. Oto one:")
    for num in guessed_nums:
        print(num)

