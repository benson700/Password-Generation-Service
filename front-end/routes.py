from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
 
app = Flask(__name__, template_folder='template', static_folder='static')
 
 
@app.route('/', methods=['POST', 'GET'])
def password_length():
   length = request.args.get('password-length')
   number = requests.post(url='http://service-2:5000/get-number',
                       json={'length': length}).json()
 
   char = requests.post(url='http://service-3:5000/get-char',
                       json={'length': length}).json()

   password = requests.post(url='http://service-4:5000/pass',
                       json={'length': length})                    
 
   return render_template('index.html', length=length)
 
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
