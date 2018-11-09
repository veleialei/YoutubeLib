import pyrebase
from flask import *

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



app = Flask(__name__)

i = 1

@app.route('/', methods=['GET', 'POST'])

def basic():
    global i
    if request.method=='POST':
        upload = request.files['upload']
        storage.child("music/test"+str(i)+".mp3").put(upload)
        i+=1
        return redirect(url_for('uploads'))
    return render_template('index.html')

@app.route('/uploads')
def uploads():
    global i
    if True:
        links = storage.child('music/test' + str(i) + '.mp3').get_url(None)
        print (links)
        return render_template('upload.html', l = links)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
