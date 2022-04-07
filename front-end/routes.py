from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
 
app = Flask(__name__, template_folder='template', static_folder='static')
 
 
@app.route('/length', methods=['POST', 'GET'])
def password_length():
   length = request.values.get('password-length')
 
   number = requests.post(url='http://service-02:5000/get-number',
                       data={'length': length}).json()
 
   char = requests.post(url='http://service-03:5000/get-char',
                       data={'length': length}).json()

   password = requests.post(url='http://service-04:5000/pass',
                       data={'length': length})                    
 
   return render_template('index.html', length=length)
 
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port='5000')
