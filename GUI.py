import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Speech_to_Text import Voice
import threading
import os

vc=Voice()
def voice():
    label.config(text="Listening... Please speak.")
    threading.Thread(target=listen).start()

def listen():
    try:
        text=vc.speech_converter()
        confirm_text(text)
    except Exception:
        label.config(text="Not audible....Try again")

def confirm_text(text):
    label.config(text="Did you say: "+text)
    label.yes_btn = tk.Button(root, text="Yes", font=("Georgia", 12), command=lambda: on_yes(text),bg="#657810")
    label.no_btn = tk.Button(root, text="No", font=("Georgia", 12), command=on_no,bg="#657810")
    label.yes_btn.pack(pady=(2,0))
    label.no_btn.pack(pady=(2,0))

def on_yes(text):
    global confirmed_text
    confirmed_text.append(text)
    label.config(text=f"Confirmed: {text}")
    label.yes_btn.destroy()
    label.no_btn.destroy()

def on_no():
    label.config(text="Please speak again.")
    label.yes_btn.destroy()
    label.no_btn.destroy()
    voice() 

root=tk.Tk()
root.geometry("600x600")
root.configure(bg="#92CD1D")
root.title("Voice-to-Text")

label = tk.Label(root, text="Welcome User", font=("Helvetica", 25), wraplength=380,bg="#92CD1D")
label.pack(pady=10)

#MicPic
base_path=os.path.dirname(__file__)
mic_path=os.path.join(base_path,"microphone-black-shape.png")
mic_pic=Image.open(mic_path)
mic_pic=mic_pic.resize((100,100))
mic_photo=ImageTk.PhotoImage(mic_pic)
mic_btn = tk.Button(root,image=mic_photo, command=voice, bg="#657810", fg="#9FACA9")
mic_btn.pack(pady=(150,50))
confirmed_text=[]

label = tk.Label(root, text="Press Mic to Speak", font=("Helvetica", 14), wraplength=380,bg="#92CD1D")
label.pack(pady=10)


root.mainloop()