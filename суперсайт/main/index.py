from flask import Flask, render_template
from flask import request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('scratch.html')


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return "Спасибо за заказ, ожидайте."


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')