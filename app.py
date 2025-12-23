from flask import Flask, redirect, render_template, request

app = Flask(__name__)

def mock_summarise(text):
    """
    Demo AI summarisation function.
    
    """
    sentences = text.split(".")
    summary = sentences[0] if sentences else text
    return f"Summary: {summary.strip()}..."

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note =request.form["note"]
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        return redirect("/")

    notes = []

    try:
        with open("notes.txt") as f:
            notes = f.readlines()
    except FileNotFoundError:
        pass
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)