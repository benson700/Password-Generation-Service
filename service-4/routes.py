from flask import Flask, Response

app = Flask(__name__)



@app.route('/', methods=['POST'])
def password():

    # combine service 2 and 3 to generate a password
    # get these two
    random_number = 0
    random_char = 0

    password = random_char + random_number

    return Response({
         'password':password
    })
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5004')