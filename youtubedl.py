from subprocess import call
# import pyrebase
# from config import Config

# firebase = pyrebase.initialize_app(Config)
# storage = firebase.storage()
def download(url):
    call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "--audio-quality", "0", "https://www.youtube.com/watch?v="+url])
    
    #storage.child("music/"+url+".mp3").put(upload)
# download("7k3rrneAFlk")
