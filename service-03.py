from flask import Flask, Response
from random import choice
import string


app = Flask(__name__)



@app.route('/', methods=['POST'])
def random_char():

    # get character length from service one
    # char = length
    digits = 0
    random_char = ''.join(choice(string.ascii_letters) for x in range(digits))

    return Response({
         'random_character':random_char
    })
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='500')