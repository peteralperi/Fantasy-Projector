
from flask import Flask, render_template, request, jsonify
from randomer import generate_random_number, store_user_input

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    number = generate_random_number()
    return jsonify(number=number)

@app.route('/store', methods=['POST'])
def store():
    user_input = request.form['user_input']
    stored_input = store_user_input(user_input)
    return jsonify(stored_input=stored_input)

if __name__ == '__main__':
    app.run(debug=True)
