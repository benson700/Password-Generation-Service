from aiohttp import request
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST'])
def password_length():
    length = request.args.get('password-length')
    # do something
    return render_template('template/index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')