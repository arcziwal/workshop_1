import random

DICE_WALLS = [3, 4, 6, 8, 10, 12, 20, 100]


def dice_string_validator(dice_str):
    dice_list = []
    for i in dice_str:
        dice_list.append(i)
    for index, value in enumerate(dice_list):
        try:
            dice_list[index] = int(value)
        except ValueError:
            continue
    d_in_list = is_d_in_dice_str(dice_str)
    how_many_dice = how_many_to_dice(dice_list)
    dice_type = which_dice(dice_list)
    correct_dice_type = is_dice_type_correct(dice_type)
    is_modification = is_modified(dice_list)
    is_sth_after_mod = last_sign(dice_list)
    mod = what_modification(dice_list, is_modification)
    dice_parameters = {
        "is D in str": d_in_list,
        "how_many_dice": how_many_dice,
        "dice_type": dice_type,
        "correct_dice_type": correct_dice_type,
        "is_modification": is_modification,
        "is_sth_after_mod": is_sth_after_mod,
        "mod": mod
    }
    #  print(dice_parameters)
    if not correct_dice_type or not is_sth_after_mod or not d_in_list:
        return False
    else:
        roll_the_dice(dice_parameters)
        return True


def is_d_in_dice_str(dice_str):
    if "D" in dice_str.upper():
        return True
    else:
        return False


def how_many_to_dice(dice_list):
    how_many_dices = []
    for a in dice_list:
        if isinstance(a, int):
            how_many_dices.append(a)
        else:
            break
    for index, value in enumerate(how_many_dices):
        how_many_dices[index] = str(value)
    how_many_dices = "".join(how_many_dices)
    if not how_many_dices:
        how_many_dices = "1"
    return how_many_dices


def which_dice(dice_list):
    where_is_d = dice_list.index("D".upper())
    number_of_dice_walls = []
    starting_index = where_is_d + 1
    for index, value in enumerate(dice_list):
        try:
            dice_list[index] = int(value)
        except ValueError:
            continue
    for i in range(3):
        try:
            if isinstance(dice_list[starting_index], int):
                number_of_dice_walls.append(dice_list[starting_index])
            else:
                break
        except IndexError:
            break
        starting_index += 1
    for index, value in enumerate(number_of_dice_walls):
        number_of_dice_walls[index] = str(value)
    number_of_dice_walls = "".join(number_of_dice_walls)
    number_of_dice_walls = int(number_of_dice_walls)
    return number_of_dice_walls


def is_modified(dice_list):
    if "+" in dice_list:
        return "+"
    elif "-" in dice_list:
        return "-"
    else:
        return False


def last_sign(dice_list):
    if dice_list[-1] == "+" or dice_list[-1] == "-":
        return False
    else:
        return True


def what_modification(dice_list, sign):
    if sign:
        how_many = []
        where_is_mod = dice_list.index(sign)
        for index, value in enumerate(dice_list):
            try:
                dice_list[index] = int(value)
            except ValueError:
                continue
        for i in dice_list[where_is_mod + 1:]:
            if isinstance(i, int):
                how_many.append(i)
        for index, value in enumerate(how_many):
            how_many[index] = str(value)
        how_many = "".join(how_many)
        how_many = int(how_many)
        return how_many
    else:
        how_many = 0
        return how_many


def is_dice_type_correct(dice_type):
    if dice_type in DICE_WALLS:
        return True
    else:
        return False


def roll_the_dice(dice_parameters):
    diced_nums = []
    for i in range(int(dice_parameters['how_many_dice'])):
        diced_nums.append(random.randint(1, dice_parameters['dice_type']))
    print(f"Wylosowane liczby to: ")
    result = 0
    for i in diced_nums:
        result += i
        print(i)
    if dice_parameters['is_modification'] == "+":
        # print(type(dice_parameters['how_many_dice']))
        # print(type(dice_parameters['dice_type']))
        # print(type(dice_parameters['mod']))
        print(f"Wynik rzutu kością (kośćmi) wynosi: {str(result + dice_parameters['mod'])}")
    elif dice_parameters['is_modification'] == "-":
        print(f"Wynik rzutu kością (kośćmi) wynosi: {str(result - dice_parameters['mod'])}")
    else:
        print(f"Wynik rzutu kością (kośćmi) wynosi: {str(result)}")
    return


data_correct = False
while not data_correct:
    try:
        dice_string = input("Podaj kod kości do gry:")
        dice_string_validator(dice_string)
    except Exception as e:
        print(f"Błąd! {e.args}")
