import tkinter as tk
import time

timer_number="0.000"
c=0

def stop():
    global c
    c=round(time.time()-c,3)

    global timer_number
    timer_number=str(c)

    global start_button
    start_button.pack_forget()
    start_button=tk.Button(root,foreground="white",activeforeground="white",background="#9B9B9B",activebackground="#9B9B9B",borderwidth=0,text="Start",font=("Arial",30),command=lambda: start())
    start_button.place(x=200,y=300,width=130,height=45)

    global timer
    timer.pack_forget()
    timer=tk.Label(root,background="#1c1c1c",foreground="white",text=c,font=("Arial",60))
    timer.place(x=0,y=80,width=800,height=75)

def start():
    global c
    c=time.time()

    global start_button
    start_button.pack_forget()
    start_button=tk.Button(root,foreground="white",activeforeground="white",background="#9B9B9B",activebackground="#9B9B9B",borderwidth=0,text="Stop",font=("Arial",30),command=lambda: stop())
    start_button.place(x=200,y=300,width=130,height=45)

def reset():
    global c
    global timer_number
    c=0
    timer_number="0.000"

    timer=tk.Label(root,background="#1c1c1c",foreground="white",text=timer_number,font=("Arial",60))
    timer.place(x=0,y=80,width=800,height=75)

    start_button=tk.Button(root,foreground="white",activeforeground="white",background="#9B9B9B",activebackground="#9B9B9B",borderwidth=0,text="Start",font=("Arial",30),command=lambda: start())
    start_button.place(x=200,y=300,width=130,height=45)

root=tk.Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("STOPWATCH")
root.configure(bg="#1c1c1c")

timer=tk.Label(root,background="#1c1c1c",foreground="white",text=timer_number,font=("Arial",60))
timer.place(x=0,y=80,width=800,height=75)

start_button=tk.Button(root,foreground="white",activeforeground="white",background="#9B9B9B",activebackground="#9B9B9B",borderwidth=0,text="Start",font=("Arial",30),command=lambda: start())
start_button.place(x=200,y=300,width=130,height=45)

reset_button=tk.Button(root,foreground="white",activeforeground="white",background="#9B9B9B",activebackground="#9B9B9B",borderwidth=0,text="Reset",font=("Arial",30),command=lambda: reset())
reset_button.place(x=460,y=300,width=130,height=45)

root.mainloop()
