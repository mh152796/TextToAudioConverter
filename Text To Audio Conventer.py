from tkinter import *
import math
from gtts import gTTS
import os
root = Tk()
root.title("Text To Audio Converter")
root.iconbitmap('d:/voiceIcon.ico')

e = Entry(root,font=('arial',50), width=18, bg='white',bd=10,  borderwidth=5, justify=RIGHT)
e.grid(row=0, column=0, columnspan=5, pady=1)



def getText():
    text = e.get()
    f = open("demofile3.txt", "w")
    f.write(text)
    f.close()
    f = open("demofile3.txt", "r")
    myText = f.read().replace("\n", " ")
    language = 'en'
    output = gTTS(text = myText, lang=language, slow=False)
    output.save("output.mp3")
    f.close()
    os.system("start output.mp3")


button = Button(root, padx=90, pady=1, bd=3, text='Convert', font=('arial', 30, 'bold'), fg='blue' , command=getText)
button.grid(row=1, column=1)
root.mainloop()
