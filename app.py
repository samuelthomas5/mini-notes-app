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
    summary = None

    if request.method == "POST":
        note =request.form["note"]
        action = request.form.get("action")

        if action == "save":
            with open("notes.txt", "a") as f:
                f.write(note + "\n")
        elif action == "Summarise":
            summary = mock_summarise(note)
        return redirect("/")

    notes = []

    try:
        with open("notes.txt") as f:
            notes = f.readlines()
    except FileNotFoundError:
        pass
    return render_template("index.html", notes=notes, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)