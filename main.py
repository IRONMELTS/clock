import tkinter as tk

def start():
    global start_button
    start_button.pack_forget()
    start_button=tk.Button(root,background="#088F8F",borderwidth=0,foreground="white",text="Stop",font=("Helvetica",30),activebackground="#088F8F",activeforeground="white",command=lambda:stop())
    start_button.place(x=200,y=300)

def stop():
    global start_button
    start_button.pack_forget()
    start_button=tk.Button(root,background="#088F8F",borderwidth=0,foreground="white",text="Start",font=("Helvetica",30),activebackground="#088F8F",activeforeground="white",command=lambda:start())
    start_button.place(x=200,y=300)

root=tk.Tk()
root.geometry('800x600')
root.title('STOPWATCH')
root.resizable(False,False)
root.configure(bg='#1c1c1c')

time=tk.Label(root,background="#1c1c1c",borderwidth=0,foreground="white",text='00.00',font=("Helvetica",60))
time.place(x=0,y=80,width=800,height=75)

start_button=tk.Button(root,background="#088F8F",borderwidth=0,foreground="white",text="Start",font=("Helvetica",30),activebackground="#088F8F",activeforeground="white",command=lambda:start())
start_button.place(x=200,y=300)

root.mainloop()
