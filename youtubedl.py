from subprocess import call
call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "--audio-quality", "0", "https://www.youtube.com/watch?v=7k3rrneAFlk"])
