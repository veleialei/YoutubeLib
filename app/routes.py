from app import app
from utility import *
from flask import render_template, request
import pyrebase
from config import Config
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(12)
firebase = pyrebase.initialize_app(Config)
storage = firebase.storage()
db = firebase.database()

@app.route('/index')
@app.route('/')
def basic():
    return render_template('index.html')

@app.route('/wishlist', methods=['GET', 'POST'])
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
    return render_template('wishlist.html', t=to.values())

@app.route('/upload', methods=['GET', 'POST'])
def uploads():
    global i
    if request.method=='POST':
        url = validate(request.form['url'])
        executor.submit(worker, url)
    return render_template('upload.html')

@app.route('/musics')
def musics():
    musics = db.child("music").get()
    urls = musics.val().values()
    links = []
    for url in urls:
        links.append(storage.child('music/' + url + '.mp3').get_url(None))
    return render_template('musics.html', l = links)

def worker(url):
    print(url)
    try:
        download(url)
        storage.child("music/"+url+".mp3").put("music/"+url+".mp3")
        db.child("music").push(url)
        print("successful")
    except:
        db.child("failure").push(url)
        print("failed")
    