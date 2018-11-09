import pyrebase

config = {
    "apiKey": "AIzaSyCK1JLNSyyAn4PQ94M_fWGLEBzm02NeMIk",
    "authDomain": "sideproject-a7c5c.firebaseapp.com",
    "databaseURL": "https://sideproject-a7c5c.firebaseio.com",
    "projectId": "sideproject-a7c5c",
    "storageBucket": "sideproject-a7c5c.appspot.com",
    "messagingSenderId": "72493675211"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method=='POST':
        upload = request.files['upload']
        storage.child("music/test.mp3").put(upload)
        return "successful"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
