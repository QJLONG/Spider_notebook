from flask import Flask, render_template, request

app = Flask(__name__)
data = [
    {"id": "1", "name": "周传雄", "num": 0},
    {"id": "2", "name": "许嵩", "num": 0},
    {"id": "3", "name": "张杰", "num": 0},
    {"id": "4", "name": "林俊杰", "num": 0}
]

@app.route("/index")
def index():
    return render_template("index.html", data=data)


@app.route("/dianzan")
def dianzan():
    id = request.args.get("id")
    data[int(id)-1]["num"] += 1
    return render_template("success.html")


app.run(debug=True)