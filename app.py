from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

notes = []
next_id = 0


@app.route("/")
def home():
    return render_template("index.html", notes=notes)


# CREATE NOTE
@app.route("/create", methods=["POST"])
def create():
    global next_id

    data = request.get_json()

    note = {
        "id": next_id,
        "content": data.get("content", ""),
        "color": data.get("color", "#fff59d"),
        "x": 100,
        "y": 100
    }

    notes.append(note)
    next_id += 1

    return jsonify(note)


# UPDATE TEXT
@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()

    for n in notes:
        if n["id"] == data["id"]:
            n["content"] = data["content"]

    return jsonify({"status": "updated"})


# DELETE NOTE
@app.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()

    global notes
    notes = [n for n in notes if n["id"] != data["id"]]

    return jsonify({"status": "deleted"})


# MOVE NOTE (DRAG SAVE POSITION)
@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()

    for n in notes:
        if n["id"] == data["id"]:
            n["x"] = data["x"]
            n["y"] = data["y"]

    return jsonify({"status": "moved"})


if __name__ == "__main__":
    app.run(debug=True)