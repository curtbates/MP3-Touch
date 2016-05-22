
import time
# from subprocess import call
# call("dir", "/b/s *.mp3 > Booklist.txt")
import os

os.system("dir /b/s *.mp3 > Booklist.txt")

f = open('Booklist.txt', 'r')
for line in f:
    myfile=line.rstrip('\n')
    if os.path.exists(myfile): 
        os.utime(myfile, None)
    print(myfile)
    time.sleep(60)
