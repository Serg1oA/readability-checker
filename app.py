# app.py
from flask import Flask, render_template, request
from readability import calculate_readability

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        scores = calculate_readability(text)
        return render_template('index.html', scores=scores, text=text)
    return render_template('index.html', scores=None, text=None)

if __name__ == '__main__':
    app.run(debug=True)