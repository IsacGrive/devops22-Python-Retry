from tkinter import *


window = Tk()
window.title("Chat program")

def send_msg():
	send = e.get()
	txt.insert(END, "\n" + send)
	e.delete(0, END)

lable = Label(window,text="Chat",pady=10, width=5, height=1).pack()

txt = Text(window, width=60)
txt.pack()

e = Entry(window,width=55)
e.pack()

send = Button(window, text="Send",command=send_msg).pack()


window.mainloop()
