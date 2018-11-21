import os
import pyrebase
from config import *
from urllib import parse
import json
import requests

firebase = pyrebase.initialize_app(Config)
storage = firebase.storage()
db = firebase.database()

keyword = "周杰伦"


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

def worker(id, did):
    print(id)
    try:
        download(id)
        storage.child("music/"+id+".mp3").put("music/"+id+".mp3")
        db.child("music").push(id)
        db.child("task").child(did).push({"id": id})

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

def searchYoutube(keyword):
    base_url = "https://www.youtube.com/watch?v="
    f = {'part' : 'snippet', 'maxResults':'25', 'q':keyword, 'key':YoutubeAPIKey}
    query = parse.urlencode(f)
    url= "https://www.googleapis.com/youtube/v3/search?" + query
    content = requests.get(url).text

    jsondata = json.loads(content)
    items = jsondata['items']
    res = []
    for i in items:
        if "videoId" in i['id']:
            print (i['id'])
            res.append(base_url + i['id']['videoId'])
    return res
    