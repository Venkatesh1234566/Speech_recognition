import speech_recognition as sr
import pyaudio
import tkinter as tk
from tkinter import *
import PIL
from PIL import Image,ImageTk

root=tk.Tk()
root.geometry("700x500")
root.title("venky")

f1=Frame(bg="#305065")
f1.place(width=700,height=500)



#initialize
#r=sr.Recognizer()

#convert Speech to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        result_label.config(text=text)
    except sr.UnknownValueError:
        result_label.config(text="I din't Recoginze Say Again")
    except sr.RequestError:
        result_label.config(text="I din't Recoginze Say Again")

logo=Image.open("C:\\Users\\VENKATESH\\OneDrive\\Pictures\\Saved Pictures\\mic.png")
resize_image=logo.resize((50,50))
img=ImageTk.PhotoImage(resize_image)





label = tk.Label(f1, text="Voice Recognition",fg="white",bg="#305065",font=("Times new roman",25))
label.place(x=220,y=50)

result_label = tk.Label(f1, text="",width=30,height=2,font=("Times new roman",15))
result_label.place(x=140,y=200)

button=Button(f1,image=img,command=recognize_speech,borderwidth=2)
button.place(x=500,y=198)


root.mainloop()

















