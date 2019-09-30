from gtts import gTTS
import os
from tkinter import *
import playsound
import speech_recognition as sr
import time
# import pyaudio
num = 1
counter = 1
speaking='speaking...'
def sayit(mytext):
    global num
    global t1

    # mytext =t1.get()

# Language in which you want to convert
    language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
    global l2
    l2.destroy()
    # t1.clear()
    t1.delete(0, END)
    t1.insert(0,mytext)
    myobj = gTTS(text=mytext, lang=language, slow=False)
    num += 1
    string=str(num)+".mp3"
    # l2.clear()
# Saving the converted audio in a mp3 file named
# welcome
    myobj.save(string)

# Playing the converted file
    playsound.playsound(string,True)
    l2 = Label(root, text=speaking)
    l2.grid(row='1', column='0')
    os.remove(string)

    time.delay(1)
    l2.destroy()
def get_audio():

    global counter

    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")  # limit 5 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        sayit(text)

    except:
        if(counter == 0) :
            sayit("Sorry, Could not understand you, will you please repeat !")

def callsay():
    try:
        sayit(t1.get())
    except:
        print("No Text to Speak")
root = Tk()
root.title("Speak It")
l1=Label(root, text = "Message :",width=20,height=5,pady=10)
t1=Entry(root,bg='black',fg='white')
b1=Button(root,text = "Say",command=callsay,pady=10,width=50)
b2=Button(root, text = 'Listen', command=get_audio,pady =10, width=50)
l2=Label(root, text='')
l1.grid(row='0',column='0')
t1.grid(row='0',column='1')
b1.grid(row='0',column='2')
l2.grid(row='1',column='0')
b2.grid(row='1',column='2')
root.mainloop()
# The text that you want to convert to audio

