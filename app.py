from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Mock AI summarization
def mock_summarize(text):
    sentences = text.split(".")
    return sentences[0].strip() + "..." if sentences[0] else "No text to summarize"

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None  # default

    # Load all notes first
    notes = []
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            notes = [n.strip() for n in f.readlines() if n.strip()]
    except FileNotFoundError:
        pass

    if request.method == "POST":
        note = request.form.get("note", "").strip()
        action = request.form.get("action")  # save or summarize

        if action == "save":
            if note:
                with open("notes.txt", "a", encoding="utf-8") as f:
                    f.write(note + "\n")
            return redirect("/")  # redirect after save

        elif action == "summarize":
            if note:
                summary = mock_summarize(note)
            else:
                summary = "Error: No text to summarize"

    return render_template("index.html", notes=notes, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)