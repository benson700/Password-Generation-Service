from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/', methods=['GET'])
def password_length():
    length = request.args.get('password-length')
    print(length)

    # do something
    # value captured from the frontend is stored in variable - length

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')