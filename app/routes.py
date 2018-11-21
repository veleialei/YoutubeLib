from app import app
from flask import render_template, request
from concurrent.futures import ThreadPoolExecutor
from utility import *

executor = ThreadPoolExecutor(12)

@app.route('/index')
@app.route('/')
def basic():
    return render_template('index.html')

@app.route('/wishlist', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        wishlist_operation(request)
    to = get_wishlist()
    if to == None:
         to = {}
    return render_template('wishlist.html', t=to.values())

@app.route('/upload', methods=['GET', 'POST'])
def uploads():
    if request.method=='POST':
        url = validate(request.form['url'])
        executor.submit(worker, url)
    return render_template('upload.html')

@app.route('/musics')
def musics():
    links = get_musics()
    return render_template('musics.html', l = links)