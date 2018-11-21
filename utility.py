import os

def download(url):
    start = "[ffmpeg] Destination: "
    command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 https://www.youtube.com/watch?v="+url #可以直接在命令行中执行的命令
    r = os.popen(command) #执行该命令
    info = r.readlines()  #读取命令行的输出到一个list
    for line in info:  #按行遍历
        line = line.strip('\r\n')
        length = len(start)
        if line.startswith(start):
            print("hahaha get you",line[length:])
            os.rename(line[length:], "music/"+url+".mp3")
# url = "7k3rrneAFlk"
# url = "-Sdq2Gk37qw"
# download(url)

def validate(url):
    res = ""
    parts = url.split("=")
    res = parts[len(parts)-1]
    return res
