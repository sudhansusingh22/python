import webbrowser
import time
import subprocess as sp

val = 0;
while(val <1):
    time.sleep(1)
    #webbrowser.open("https://www.youtube.com/watch?v=dO1rMeYnOmM")
    child = sp.Popen("google-chrome %s" % "https://www.youtube.com/watch?v=dO1rMeYnOmM", shell=True)
    val = val +1
    
