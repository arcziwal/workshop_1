from flask import Flask, request

HTML_START = """
<!DOCTYPE html>
<html lang="pl-PL">
<head>
    <meta charset="UTF-8">
    <title>Zgaduję numer</title>
</head>
<body>
    <h2>Wymyśl liczbę od 1 do 1000 a zgadnę ją w 10 próbach</h2>
    <form action="" method="POST">
        <input type="hidden" name="min" value="{}">
        <input type="hidden" name="max" value="{}">
        <input type="submit" value="OK">
    </form>
</body>
</html>
"""

HTML = """
<!DOCTYPE html>
<html lang="pl-PL">
<head>
    <meta charset="UTF-8">
    <title>Am I correct</title>
</head>
<body>
    <h2>Czy ten numer to {}?</h2>
    <form action="" method="POST">
        <input type="submit" name="user_answer" value="za wysoki">
        <input type="submit" name="user_answer" value="za niski">
        <input type="submit" name="user_answer" value="zgadłeś!">
        <input type="hidden" name="min" value="{min}">
        <input type="hidden" name="max" value="{max}">
        <input type="hidden" name="guess" value="{guess}">
    </form>
</body>
</html>        
"""

HTML_WIN = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>I won!</title>
</head>
<body>
    <h1>Wygrałem! Twój numer to {}</h1>
</body>
</html>
"""

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def number_guess():
    if request.method == "GET":
        return HTML_START.format(0, 1000)
    elif request.method == "POST":
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "za wysoka":
            max_number = guess
        elif user_answer == "za niska":
            min_number = guess
        elif user_answer == "zgadłeś!":
            return HTML_WIN.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return HTML.format(guess=guess, min=min_number, max=max_number)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
