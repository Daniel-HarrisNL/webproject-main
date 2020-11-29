import os
#import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cases')
def cases():
    return render_template('cases.html')

@app.route('/item')
def item():
    return render_template('item.html')

@app.route('/dino')
def dino():
    return render_template('dino.html')

@app.route('/blueprint')
def blueprint():
    return render_template('blueprint.html')

    
if __name__ == '__main__':
    #Inbound setting in EC2 must be set up with Custom TCP Rule, Port range 8080, Source = Anywhere
    app.run(host='0.0.0.0', port=8080, debug=True)