import os
import pyrebase
from config import Config

firebase = pyrebase.initialize_app(Config)
storage = firebase.storage()
db = firebase.database()

def download(url):
    start = "[ffmpeg] Destination: "
    command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 https://www.youtube.com/watch?v="+url #可以直接在命令行中执行的命令
    r = os.popen(command) 
    info = r.readlines() 
    for line in info:
        line = line.strip('\r\n')
        length = len(start)
        if line.startswith(start):
            print("hahaha get you",line[length:])
            os.rename(line[length:], "music/"+url+".mp3")

def validate(url):
    res = ""
    parts = url.split("=")
    res = parts[len(parts)-1]
    return res

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

def get_musics():
    musics = db.child("music").get()
    urls = musics.val().values()
    urls = set(urls)
    links = []
    for url in urls:
        links.append(storage.child('music/' + url + '.mp3').get_url(None))
    return links

def wishlist_operation(request):
    if request.form['submit'] == 'add':
        name = request.form['name']
        db.child("todo").push(name)
    elif request.form['submit'] == 'delete':
        name = request.form['name']
        db.child("todo").remove()

def get_wishlist():
    todo = db.child("todo").get()
    to = todo.val()
    return to