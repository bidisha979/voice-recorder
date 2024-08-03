import sounddevice
import os
from scipy.io.wavfile import write
import time as t
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askdirectory

folder = ""

def file_folder():
    global folder
    folder = askdirectory()
    if not folder:
        showwarning(title="Folder Selection", message="Please select a folder.")
    else:
        location.config(text=os.path.basename(folder))

def save_file():
    global folder
    if not folder:
        showwarning(title="Folder Selection", message="Please select a folder.")
        return

    try:
        file = file_name.get()

        if not file:
            showwarning(title="File Name", message="Please enter a file name.")
            return
        file_path = f"{folder}/{file}.wav"

        if os.path.exists(file_path):
            showwarning(title="File Exists", message="A file with the same name already exists in the folder.")
            return
        
        time = int(timeInbox.get())
        showinfo(title="Start", message="Start Recording")
        Record = sounddevice.rec((time * 44100), samplerate=44100, channels=2)

        while time>0:
            interface.update()
            t.sleep(1)
            time-=1
            if(time==0):
                messagebox.showinfo("End", "Recording Completed")
            Label(text=f"{str(time)}", font="arial 40", width=4, background="#4a4a4a").place(x=112,y=435)

        sounddevice.wait()
        write(file_path, 44100, Record)
        # showinfo(title="End", message="Recording Completed")

    except ValueError:
        showwarning(title="Time Error", message="Invalid time format. Please enter time in seconds.")

def mainInterface():
    global timeInbox, file_name, location, interface

    interface = Tk()
    interface.geometry("350x510")
    interface.resizable(False, False)
    interface.title("Voice Recorder")
    interface.config(bg="#4a4a4a")

    micImg = PhotoImage(file="mic2.png")
    interface.iconphoto(False, micImg)
    startButton = Button(interface, image=micImg, background="#4a4a4a", command=save_file)
    startButton.place(x=80, y=30)

    location = Button(interface, text="Select Folder", font=("Time New Roman", 12), command=file_folder)
    location.place(x=101, y=240, height=40, width=150)

    label3 = Label(interface, text="Enter file name :", font=("Time New Roman", 12), bg="#4a4a4a", fg="White")
    label3.place(x=117, y=290)

    file_name = Entry(interface, font=("Time New Roman",12))
    file_name.place(x=100, y=320, height=30, width=150)

    label2 = Label(interface, text="Enter time (in sec) :", font=("Time New Roman", 12), bg="#4a4a4a", fg="White")
    label2.place(x=106, y=360)

    timeInbox = Entry(interface, font=(20))
    timeInbox.place(x=148, y=390, height=40, width=55)

    interface.mainloop()

mainInterface()