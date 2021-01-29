from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<dark>')
def mode(dark):
    return render_template('index.html', mode=dark)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
