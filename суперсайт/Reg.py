from flask import Flask, url_for
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации и покупки</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="secname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="secname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <div>
                                    <label for="classSelect"> </label>
                                    <label for="classSelect"> </label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                      <label class="form-check-label" for="female">
                                        SberPay
                                      </label>
                                    </div>
                                    <div>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                      <label class="form-check-label" for="female">
                                        Tinkoff
                                      </label>
                                    </div>
                                    <div>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                      <label class="form-check-label" for="female">
                                        Visa
                                      </label>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Номер карты</label>
                                        <textarea class="form-control" id="about" rows="1" name="about"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Соглашаюсь с покупкой</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Купить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['secname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена, вы человек"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')