from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
 
 
@app.route('/pass', methods=['POST'])
def password():
 
   # combine service 2 and 3 to generate a password
   # get these two
   random_number = request.get_json()['random_num']
   random_char =  request.get_json()['random_char']
 
   password = random_char + random_number
 
   return jsonify(password=password)
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')