import tkinter
import sys
import textwrap
from mutagen.mp3 import MP3 as mp3
import pygame
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk,Image
import time
import threading
import re
from numpy.random import *
isss = None
itii = None

def end():
    root.destroy()
    pygame.mixer.music.stop()
    itii == "abcd"
    filename = '02.mp3' #再生したいmp3ファイル
    pygame.mixer.init()
    pygame.mixer.music.load(filename) #音源を読み込み
    mp3_length = mp3(filename).info.length #音源の長さ取得
    pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
    time.sleep(9.2)
    itii == "abcd"
    pygame.mixer.music.stop()


filename = '001.mp3' #再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename) #音源を読み込み
mp3_length = mp3(filename).info.length #音源の長さ取得
pygame.mixer.music.play(100) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
root = tkinter.Tk()
root.title(u"緊急地震速報")
root.geometry("550x300")
root.attributes('-topmost', True)
text="".join(sys.argv).replace("window.py","").replace(":pp:","\n").replace("#緊急地震速報#地震","").replace("-","").replace(sys.argv[-1],"")
text=re.sub('あと[0-9][0-9]秒',"",text)
text=re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
Static1 = tkinter.Label(text=text,font=("",20))
Static1.pack()
Button = tkinter.Button(text=u'確認',command=end,width=100,height=25,bg = '#7289da')
Button.pack()
root.mainloop()

