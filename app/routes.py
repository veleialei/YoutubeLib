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
    id = ""
    did = ""
    if request.method == 'GET':
        id = request.args.get('id')
        did = request.args.get('did')
        executor.submit(worker, id, did)
    if request.method == 'POST':
        id = request.form['id']
        did = "1A8ED76C-3B48-499A-8298-08A6CB8BFB41"
        executor.submit(worker, id, did)
    return render_template('upload.html')

@app.route('/musics')
def musics():
    links = get_musics()
    return render_template('musics.html', l = links)

@app.route('/search', methods=['GET', 'POST'])
def search():
    links = []
    if request.method=='POST':
        keyword = request.form['keyword']
        links = searchYoutube(keyword)
    return render_template('search.html', l = links)