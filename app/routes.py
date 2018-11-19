from app import app
from flask import render_template, request
import pyrebase
from config import Config

firebase = pyrebase.initialize_app(Config)
storage = firebase.storage()
db = firebase.database()

i = 1

@app.route('/', methods=['GET', 'POST'])
def basic():
    return render_template('index.html')

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name = request.form['name']
            db.child("todo").push(name)
        elif request.form['submit'] == 'delete':
            name = request.form['name']
            db.child("todo").remove()
    todo = db.child("todo").get()
    to = todo.val()
    if to == None:
         to = {}
    return render_template('todo.html', t=to.values())

#就是显示媒体库里面有多少
@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    global i
    if request.method=='POST':
        name = request.form['name']
        print(name)
        # upload = request.files['upload']
        # storage.child("music/test"+str(i)+".mp3").put(upload)
        # i+=1
    links = []
    for id in range(1,3):
        links.append(storage.child('music/test' + str(id) + '.mp3').get_url(None))
    return render_template('upload.html', l = links)

