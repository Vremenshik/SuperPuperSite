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
                                    Спасибо за покупку
                                    <button type="submit" class="btn btn-primary">Назад</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена, вы человек"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')