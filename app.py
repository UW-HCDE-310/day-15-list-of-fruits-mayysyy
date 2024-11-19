from flask import Flask, render_template
import keys
app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

    filtered_fruits_o = []
    for fruit in fruits:
        if fruit.get("name", "").startswith("o"):
            filtered_fruits_o.append(fruit["name"])

    more_than_three = []
    for fruit in fruits:
        if fruit.get("quantity", 0) > 3:
            more_than_three.append(fruit["name"])

    return render_template("index.html", fruits=fruits, key_1=keys.MY_SECRET_API_KEY_1, key_2=keys.MY_SECRET_API_KEY_2,)
    # return render_template("index.html", filtered_fruits_o=filtered_fruits_o)