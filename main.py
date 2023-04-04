from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Frances")


@app.route("/test")
def test():
    return render_template("index.html", name="Test ok")

@app.route("/tipp")
def tipp_des_tages():
    tipps = ["Tipp 1", "Tipp 2", "Tipp 3"]
    return render_template("tdt.html", tipp=tipps[0])


if __name__ == "__main__":
    app.run(debug=True, port=5001)