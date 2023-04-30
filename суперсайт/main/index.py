from flask import Flask, render_template
from flask import request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('scratch.html')


@app.route('/s')
def index2():
    global login
    login = False
    return render_template('scratch.html')


login = False


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    global login
    if request.method == 'GET' and login == False:
        return render_template('login.html')
    elif request.method == 'POST':
        login = True
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                                    Спасибо за покупку
                                    <a href="/" class="button">Назад</a>
                                </form>
                            </div>
                          </body>
                        </html>'''
    else:
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                                    Вы уже авторизованы
                                    <a href="/" class="button">Назад</a><br>
                                    <a href="/s" class="button">Выйти</a>                                    
                                </form>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')