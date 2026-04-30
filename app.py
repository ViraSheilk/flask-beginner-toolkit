from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []
next_id = 0  # ensures unique IDs

@app.route("/", methods=["GET", "POST"])
def home():
    global next_id

    if request.method == "POST":
        content = request.form.get("note")
        color = request.form.get("color")

        if content:
            notes.append({
                "id": next_id,
                "content": content,
                "color": color if color else "#ffff88"
            })
            next_id += 1

    return render_template("index.html", notes=notes)


# DELETE
@app.route("/delete/<int:id>")
def delete(id):
    global notes
    notes = [note for note in notes if note["id"] != id]
    return redirect("/")


# EDIT (load edit page)
@app.route("/edit/<int:id>")
def edit(id):
    note_to_edit = None
    for note in notes:
        if note["id"] == id:
            note_to_edit = note
            break

    return render_template("edit.html", note=note_to_edit)


# UPDATE (save changes)
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    for note in notes:
        if note["id"] == id:
            note["content"] = request.form.get("note")
            note["color"] = request.form.get("color")
            break

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)