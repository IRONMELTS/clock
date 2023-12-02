import tkinter as tk
import time

timer_number=0
c=0
save=0
just_started=True

def start():
      global c,just_started,start_button,show_time,loop

      if just_started==True:
            c+=time.time()
            start_button.pack_forget()
            start_button=tk.Button(root,text="Stop",font=("Arial",30),background="#2ecc71",activebackground="#2ecc71",foreground="white",activeforeground="white",border=0,command=lambda: stop())
            start_button.place(x=190,y=300,height=50,width=100)
            just_started=False

      show_time.pack_forget()
      diff=round(time.time()-c,3)
      show_time=tk.Label(root,text=diff,font=("Arial",60),background="#1c1c1c",foreground="white")
      show_time.place(x=0,y=100,width=800,height=80)
      loop=root.after(10,start)

def stop():
      global start_button,just_started,save
      root.after_cancel(loop)
      save=time.time()-c

      start_button.pack_forget()
      start_button=tk.Button(root,text="Start",font=("Arial",30),background="#2ecc71",activebackground="#2ecc71",foreground="white",activeforeground="white",border=0,command=lambda: start())
      start_button.place(x=190,y=300,height=50,width=100)
      just_started=True

def reset():
      try:
            root.after_cancel(loop)
      except:
            pass
      global timer_number,start_button,show_time,c
      timer_number=0
      c=0

      start_button.pack_forget()
      show_time.pack_forget()

      show_time=tk.Label(root,text=timer_number,font=("Arial",60),background="#1c1c1c",foreground="white")
      show_time.place(x=0,y=100,width=800,height=80)

      start_button=tk.Button(root,text="Start",font=("Arial",30),background="#2ecc71",activebackground="#2ecc71",foreground="white",activeforeground="white",border=0,command=lambda: start())
      start_button.place(x=190,y=300,height=50,width=100)


root=tk.Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("TEST")
root.configure(background="#1c1c1c")

show_time=tk.Label(root,text=timer_number,font=("Arial",60),background="#1c1c1c",foreground="white")
show_time.place(x=0,y=100,width=800,height=80)

start_button=tk.Button(root,text="Start",font=("Arial",30),background="#2ecc71",activebackground="#2ecc71",foreground="white",activeforeground="white",border=0,command=lambda: start())
start_button.place(x=190,y=300,height=50,width=100)

reset_button=tk.Button(root,text="Reset",font=("Arial",30),background="#2ecc71",activebackground="#2ecc71",foreground="white",activeforeground="white",border=0,command=lambda: reset())
reset_button.place(x=510,y=300,height=50,width=120)

root.mainloop()
