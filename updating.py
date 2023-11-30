import tkinter as tk

timer_number=0

def start():
    global timer_number
    timer_number+=1
    global timer
    timer.pack_forget()
    timer=tk.Label(root,background="#1c1c1c",foreground="white",text=timer_number,font=("Arial",60))
    timer.place(x=0,y=80,width=800,height=75)
    root.after(1000,start)

root=tk.Tk()
root.title("TEST")
root.geometry("800x600")
root.configure(background="#1c1c1c")

timer=tk.Label(root,background="#1c1c1c",foreground="white",text=timer_number,font=("Arial",60))
timer.place(x=0,y=80,width=800,height=75)

start()

root.mainloop()
