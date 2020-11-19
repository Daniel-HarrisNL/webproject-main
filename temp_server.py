import os
#import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
if __name__ == '__main__':
    #Inbound setting in EC2 must be set up with Custom TCP Rule, Port range 8080, Source = Anywhere
    app.run(host='0.0.0.0', port=8080, debug=True)