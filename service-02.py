from flask import Flask, Response
from random import randint


app = Flask(__name__)



@app.route('/', methods=['POST'])
def random_num():

    # get digits from service one
    # digits = length
    digits = 0
    random_num = ''.join(["{}".format(randint(0, digits)) for num in range(0, digits)])
    
    return Response({
         'random_number':random_num
    })
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5002')