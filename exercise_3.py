print("Pomyśl liczbę od 0 do 1000 a ja zgadnę w max 10 próbach")
min_num = 0
max_num = 1000

success = False
while not success:
    guess_num = int((max_num - min_num) / 2) + min_num
    print(f"Zgaduję: {guess_num}")
    print("""
    Wpisz "za dużo" jeśli moja liczba jest za duża
    Wpsiz "za mało" jeśli moja liczba jest za małą
    Wpisz "zgadłeś" jeśli odgadłem liczbę
    """)
    try:
        user_answer = input()
        if user_answer == "zgadłeś":
            success = True
        elif user_answer == "za dużo":
            max_num = guess_num
            continue
        elif user_answer == "za mało":
            min_num = guess_num
            continue
        else:
            raise Exception
    except Exception:
        print("To nie jest prawidłowa odpowiedź. Spróbuj ponownie!")
        continue
    print("Dziękuję za grę!")
