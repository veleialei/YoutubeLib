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

db = firebase.database()

#db.child("id_record").push({"value":"0"})

#db.child("names").child("name").update({"name":"shuangjiao"})

# users = db.child("names").child("name").get()
# print(users.key())
# print(users.val())

#users = db.child("names").child("name").remove()

users = db.child("names").remove()
app = Flask(__name__)

i = 1

@app.route('/', methods=['GET', 'POST'])
def basic():
    return render_template('index.html')
    
#此处要改成接受 youtube link
#然后接收了立刻 download到本地
#然后传到 storage 里面
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
@app.route('/uploads')
def uploads():
    global i
    if request.method=='POST':
        upload = request.files['upload']
        storage.child("music/test"+str(i)+".mp3").put(upload)
        i+=1
    links = []
    for id in range(1,3):
        links.append(storage.child('music/test' + str(id) + '.mp3').get_url(None))
    return render_template('upload.html', l = links)

if __name__ == '__main__':
    app.run(debug=True)
