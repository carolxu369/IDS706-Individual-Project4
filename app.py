from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load text summarization model from Hugging Face
summarizer = pipeline("summarization")

@app.route("/")
def index():
    # Render the initial form for input
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    if request.method == "POST":
        text = request.form["text"]
        # Perform text summarization on the provided text
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        summarized_text = summary[0]["summary_text"]
        # Render the results along with the input text
        return render_template("result.html", original_text=text, summarized_text=summarized_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
