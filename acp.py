from tkinter import *
import random
root = Tk()
root.geometry("300x300")

root.title("Rps Game vs AI")

computer_value = {
    "0":"Rock",
    "1" :"Paper",
    "2"  : "Scissors"
}

def reset_game():
    b1["state"] =  "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.congig(text="Player")
    l3.config(text="Computer")
    l4.config(text="")
    
def button_disable():
    b1["state"] =  "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"

def isrock():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v =="Scissors":
        match_result = "Player win"
    else:
        match_result = "Computer win"
    l4.config(text=match_result)
    l3.config(text=c_v)
    button_disable()

def isscissors():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Computer win"
    elif c_v =="Scissors":
        match_result = "Draw"
    else:
        match_result = "player win"
    l4.config(text=match_result)
    l3.config(text=c_v)
    button_disable()
def ispaper():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Player win"
    elif c_v =="Scissors":
        match_result = "Computer win"
    else:
        match_result = "Match draw"
    
    l4.config(text=match_result)
    l3.config(text=c_v)
    button_disable()

Label(root,text="RPS",font="Arial",fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,text = "Player",font="Arial")
l2 = Label(frame,text = "Vs",font="Arial")
l3 = Label(frame,text = "Computer",font="Arial")

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,text = "",bg="white",width=15,borderwidth=2,relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1,text = 'Rock',font=18,width=7,command = isrock)
b2 = Button(frame1,text = 'Scissors',font=18,width=7,command = isscissors)
b3 = Button(frame1,text = 'Paper',font=18,width=7,command = ispaper)

b1.pack(side=LEFT,padx = 10)
b2.pack(side=LEFT,padx=10)
b3.pack(padx=10)

Button(root,text="Reset Game", font=10,fg="red",bg="black",command=reset_game).pack(pady=20)
root.mainloop()