import http.client
import random

from flask import Flask, render_template

app = Flask(__name__)

words = {"one": "один", "two": "два", "three": "три"}

lists = [23, 16, 144, 72, 90, 11, 5]
words2 = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]
content = "Кот это не хлеб, подумай, не ешь его, разработчик! Ай, ну я же просил"


@app.route('/')
def page_index():
    return render_template('main.html')


@app.route('/hello/')
def hello():
    return ("hello"
            '<p><a href="/">На главную</a></p>')


@app.route('/goodbye/')
def goodbye():
    return ("goodbye"
            '<p><a href="/">На главную</a></p>')


@app.route('/seeyou/')
def seeyou():
    return ("seeyou"
            '<p><a href="/">На главную</a></p>')


@app.route('/random/')
def random_func():
    s = random.randint(1, 10)
    return (f'{str(s)}'
            '<p><a href="/">На главную</a></p>')


@app.route('/first/')
def first():
    '''
        Выводит первое число из списка
    '''

    return (f'{str(lists[0])}'
            '<p><a href="/">На главную</a></p>')


@app.route('/last/')
def last():
    '''
        Выводит последнее число из списка
    '''

    return (f'{str(lists[-1])}'
            '<p><a href="/">На главную</a></p>')


@app.route('/sum/')
def sum_func():
    '''
        Выводит сумму чисел из списка
    '''

    return (f'Список из чисел: {" + ".join(map(str, lists))}\n'
            f'<br>Равно = {str(sum(lists))}'
            '<p><a href="/">На главную</a></p>')


@app.route('/mentions/')
def mentions():
    '''
        Выводит все слова из списка, начинающиеся на @
    '''
    f = []
    for i in words2:
        if i[0] == '@':
            f.append(i[1:])

    return (f'Список слов: {", ".join(words2)}<br>'
            '<br>'
            f'<b>Результат:</b> {", ".join(f)}<br>'
            '<p><a href="/">На главную</a></p>')


@app.route('/words/')
def words():
    '''
        подсчитывает слова, например:  11 слов
    '''
    index = 0
    for i in content:
        if i == ' ':
            index += 1
    return (f'<b>Предложение:</b> {content}<br>'

            f'В предложении: {index + 1} слов<br>'
            '<br>'
            '<p><a href="/">На главную</a></p>')


@app.route('/spaces/')
def spaces():
    '''
        подсчитывает пробелы, например 10 пробелов
    '''
    index = 0
    for i in content:
        if i == ' ':
            index += 1
    return (f'<b>Предложение:</b> {content}<br>'
            f'В предложении: {index} пробелов<br>'
            '<br>'
            '<p><a href="/">На главную</a></p>')


@app.route('/letters/')
def letters():
    '''
        подсчитывает пробелы, например 10 пробелов
    '''
    index = 0
    symbol = [' ', '!', ',']
    for i in content:
        if i not in symbol:
            index += 1
    return (f'<b>Предложение:</b> {content}<br>'

            f'В предложении: {index} букв<br>'
            '<br>'
            '<p><a href="/">На главную</a></p>')


@app.route('/ip/')
def ip():
    '''
        Получаем внешний IP
    '''
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    s = conn.getresponse().read()
    s = str(s)
    return (f'Ваш IP адрес: {s[2:-1]}'
            '<br>'
            '<p><a href="/">На главную</a></p>')


app.run(debug=True, port=8000)
