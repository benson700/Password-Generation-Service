from flask import Flask, jsonify, request
from random import randint
import requests
 
app = Flask(__name__)
 
 
 
@app.route('/get-number', methods=['POST'])
def random_num():
 
   # get digits from service one
   digits = request.get_json()['length']
 
   random_num = ''.join(["{}".format(randint(0, digits)) for num in range(0, digits)])
 
   requests.post(url='http://service-04:5000/pass',
                       data={'random_num': random_num})
 
   return jsonify(random_num=random_num)
      
  
 
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')