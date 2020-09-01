from flask import Flask, render_template, request
import random

DEBUG = True
app = Flask(__name__)

@app.route("/rechnen", methods=["GET","POST"])
def stelle_aufgabe():
    
    return render_template(
        "rechnen.html",
        a = random.randint(0,9),
        b = random.randint(0,9)
    )


if __name__ == "__main__":
    app.run()
