
from flask import Flask, render_template, request, jsonify
from analyze import store_user_input

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def store():
    user_input = request.form['user_input']
    score = store_user_input(user_input)
    return jsonify(score=score)

if __name__ == '__main__':
    app.run(debug=True)
