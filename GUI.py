import tkinter as tk
from PIL import Image, ImageTk
from Speech_to_Text import Voice
import threading
import os
from parse import PersonalInfo,Diagnosis
from database import Appointments

vc=Voice()
patient_name=""
patient_symptoms=""
patient_appoint_date=""
patient_gender=""
patient_address=""
patient_age=""

def voice():
    global t
    if(t%3==1):
        label.config(text="Give Personal info of patient")
    elif(t%3==2):
        label.config(text="Tell the symptoms")
    elif(t%3==0):
        label.config(text="Give the appointment date")
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
    global personal_info
    global symptoms
    global appointment_date
    global t
    confirmed_text.append(text)
    label.config(text=f"Confirmed: {text}")
    label.yes_btn.destroy()
    label.no_btn.destroy()
    if(t%3==1): 
        personal_info = PersonalInfo.extract_info(text)
        t+=1
        voice()
    elif(t%3==2):
        symptoms = Diagnosis.extract_symptoms(text)
        t+=1
        voice()
    elif(t%3==0):
        appointment_date = Diagnosis.extract_appointment_date(text)
        t+=1
    if(t%4==0):
        display_full_info(personal_info,symptoms,appointment_date)
    return confirmed_text

def on_no():
    label.config(text="Please speak again.")
    label.yes_btn.destroy()
    label.no_btn.destroy()
    voice() 

def display_full_info(personal_info, symptoms, appointment_date):

    global patient_name
    global patient_symptoms
    global patient_appoint_date
    global patient_age
    global patient_address
    global patient_gender
    # Remove previous info labels
    for widget in root.pack_slaves():
        if isinstance(widget, tk.Label) and widget.cget("fg") == "blue":
            widget.destroy()

    tk.Label(root, text="--- Personal Info ---", fg="#060900", font=("Helvetica", 14), bg="#92CD1D").pack()
    for key, value in personal_info.items():
        tk.Label(root, text=f"{key}: {value}", fg="#060900", font=("Helvetica", 12), bg="#92CD1D").pack()

    tk.Label(root, text="--- Diagnosis ---", fg="#060900", font=("Helvetica", 14), bg="#92CD1D").pack()

    if symptoms:
        for symptom, dept in symptoms:
            tk.Label(root, text=f"{symptom.title()} → {dept}", fg="#060900", font=("Helvetica", 12), bg="#92CD1D").pack()
    else:
        tk.Label(root, text="No symptoms detected.", fg="#060900", font=("Helvetica", 12), bg="#92CD1D").pack()
    
    tk.Label(root, text=f"Appointment Date: {appointment_date}", fg="#060900", font=("Helvetica", 12), bg="#92CD1D").pack()
    
    patient_name = personal_info.get("Name", "Unknown")
    patient_gender = personal_info.get("Gender", "Unknown")
    patient_age = personal_info.get("Age", "Unknown")
    patient_address = personal_info.get("Address", "Unknown")
    patient_symptoms = [s[0] for s in symptoms] if symptoms else []
    patient_appoint_date = appointment_date

    #if patient_name and patient_symptoms and appointment_date  and patient_gender and patient_address and = "Not specified":
    Appointments.save_appointment(patient_name,patient_age,patient_gender,patient_address, patient_symptoms, appointment_date)
    tk.Label(root, text="Appointment saved to Excel!", fg="#1A0E85", font=("Helvetica", 12), bg="#92CD1D").pack(pady=10)
    # else:
    #     tk.Label(root, text="Unable to save appointment: Missing info", fg="#CB0505", font=("Helvetica", 12), bg="#92CD1D").pack(pady=10)


#Code starts here

root=tk.Tk()
root.geometry("600x600")
root.configure(bg="#92CD1D")
root.title("Voice-to-Text")

label = tk.Label(root, text="Welcome User", font=("Helvetica", 25), wraplength=380,bg="#92CD1D")
label.pack(pady=10)

t=1
personal_info=""
symptoms=""
appointment_date=""

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