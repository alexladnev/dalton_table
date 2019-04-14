from flask import *
from galtons_table import get
from different_chances import ggg
from line import ggggg
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def goto():
    return redirect("/galtons_table")

@app.route("/galtons_table", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        number = request.form["stringi1"]
        count = request.form["stringi2"]
        result = get(int(number), int(count))
        return render_template("result.html", result=result)
    return render_template("dalton.html")

@app.route("/different", methods=["GET", "POST"])
def chance():
    if request.method == "POST":
        number = int(request.form["stringi1"])
        count = int(request.form["stringi2"])
        prob = list(map(float, request.form["stringi3"].split(", ")))
        result = ggg(number, count, prob)
        return render_template("result.html", result=result)
    return render_template("pohui.html")


@app.route("/line", methods=["GET", "POST"])
def line():
    if request.method == "POST":
        number = int(request.form["stringi1"])
        result = ", ".join(list(map(str, ggggg(number))))
        return render_template("hui.html", result=result)
    return render_template("line.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=33507)
