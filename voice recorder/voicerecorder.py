import sounddevice
from scipy.io.wavfile import write
from tkinter import *

from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory
add=""
def file_path():
    global add
    add = askdirectory()

def save_file():
    global add
    try:
        time = int(sec.get())
        addr = add +"/"+"audio1.wav"
        showinfo(title="Start",message="Recording Started")
        recording = sounddevice.rec((time*44100),samplerate=44100,channels=2)
        sounddevice.wait()
        write(addr,44100,recording)
        showinfo(title="End",message="recorded successfully")
    except:
        showwarning(title="Time",message="Wrong format")
def main_window():
    global sec
    win=Tk()
    win.geometry("400x600")
    win.resizable(False,False)
    win.title("Voice Recorder")
    win.config(background="#7393B3")

    img1=PhotoImage(file="blue.png")
    l1= Label(win,image=img1)
    l1.place(x=40,y=20,height=200,width=300)

    sec = Entry(win,font=(20))
    sec.place(x=140,y =300, height=50, width=100)
    l2 = Label(win,text="Time: Secs", font=("Times New Roman", 16), background="#7393B3")
    l2.place(x= 40, y=350,height=40, width=300)

    b=Button(win,text="Specify Path",font=("Times New Roman", 15),command=file_path)
    b.place(x=110, y=420,height=40, width=150)


    start = Button(win,text="Start", background="#7393B3",foreground="white",command=save_file)
    start.place(x=130, y=480, height=30, width=100)
    win.mainloop()
main_window()


