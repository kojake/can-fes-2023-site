import vote_calculation
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def call():
    return render_template("index.html", test=vote_calculation.get_votes())
    


if __name__ == "__main__":
    app.run(debug=True)