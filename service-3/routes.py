from flask import Flask, jsonify, request
from random import choice
import string
import requests
 
 
app = Flask(__name__)
 
 
 
@app.route('/get-char', methods=['POST'])
def random_char():
 
   # get character length from service one
   digits = request.get_json()['length']
   random_char = ''.join(choice(string.ascii_letters) for x in range(digits))
 
   requests.post(url='http://service-04:5000/pass',
                       data={'random_char': random_char})
 
   return jsonify(random_char=random_char)
       
  
  
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')