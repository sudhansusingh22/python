import webbrowser
import time
import random
import string
import subprocess as sp
import os

# for firefox browser replace this variable with 'firefox'
browserExe = "chrome"

# read randdom lines from file
lines = open('words.txt').read().splitlines()
words = []
for i in range(30):
	words.append(random.choice(lines))
print(len(words))


def browse(url, how_long):
    #for firefox replace it with firefox
    child = sp.Popen("google-chrome %s" % url, shell=True)
    time.sleep(how_long)
    child.terminate()

# go to bing.com search for cat and copy the url to oldString
# you should be logged in to your microsoft account

oldString = ""
oldString = string.replace(oldString, 'cat', words[0])

browse(oldString, 5)

for i in range(1,30):
	oldWord = words[i-1]
	newWord = words[i]
	newString = string.replace(oldString, oldWord, newWord)
	oldString = newString
	browse(newString,5)


time.sleep(5)
os.system("pkill "+browserExe)
