from tkinter import *
import os
root=Tk()
root.title("Arcade-o-Matic by Count Gameula")
root.iconbitmap("assets/Arcade-o-Matic Logo 3.ico")
bg=PhotoImage(file="assets/BG1.png")
#defining button functions
def cricket():
    os.system('start cmd /c "python Cricket.py"')
def ttt():
    os.system('start cmd /c "python Tictactoe.py"')
def rps():
    os.system('start cmd /c "python rps.py"')
def bb():
    os.system('start cmd /c "python Baseball.py"')
def tet():
    os.system('start cmd /c "python Tetris.py"')
def sud():
    os.system('start cmd /c "python Sudoku1.py"')
def snk():
    os.system('start cmd /c "python Snake.py"')
def unsc():
    os.system('start cmd /c "python Unscramble.py"')
lblbg=Label(root,image=bg).place(x=0,y=0)
spacey_label0=Label(root,text="",bg="#c6e22d").grid(row=0,columnspan=5)
#basic info
arc_o_mat=Label(root, text="Arcade-o-Matic", bg="black", fg="cyan").grid(row=1,column=2)
tg_ln=Label(root, text="A Walk Down the Memory Lane - A Simpler Life",justify="center",fg="red",bg="#c6e22d").grid(row=2,columnspan=5)
spacey_label1=Label(root,text="",bg="#c6e22d").grid(row=3,columnspan=5)
info_label=Label(root,text="Find a collection of games that everyone loves. Play them at your convinience and enjoy to your heart's content!",fg="blue").grid(row=4,columnspan=5)
spacey_label2=Label(root,text="",bg="#c6e22d").grid(row=5,columnspan=5)
question_label=Label(root, text="What game would you like to play?",fg="blue",bg="#c6e22d").grid(row=6,column=2)
spacey_label3=Label(root,text="",bg="#c6e22d").grid(row=7,columnspan=5)
#button row 1
oddeve_button=Button(root,text="Cricket",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",padx=36,command=cricket).grid(row=8,column=0)
tictactoe_button=Button(root,text="Tic-Tac-Toe",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",padx=23,command=ttt).grid(row=8,column=2)
stonepaperscissor_button=Button(root,text="Stone-Paper-Scissor",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",command=rps).grid(row=8,column=4)
spacey_label4=Label(root,text="",bg="#c6e22d").grid(row=9,columnspan=5)
#button row 2
baseball_button=Button(root,text="Baseball",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",padx=33,command=bb).grid(row=10,column=1)
tetris_button=Button(root,text="Tetris",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",padx=40,command=tet).grid(row=10,column=3)
spacey_label5=Label(root,text="",bg="#c6e22d").grid(row=11,columnspan=5)
#button row 3
sudoku_button=Button(root,text="Sudoku",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",padx=34,command=sudo).grid(row=12,column=0)
snake_button=Button(root,text="Snake",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",padx=39,command=snk).grid(row=12,column=2)
unscramble_button=Button(root,text="Unscramble",bg="black",fg="white",activebackground="gray",activeforeground="pink",bd=10,highlightcolor="pink",padx=23,command=unsc).grid(row=12,column=4)
spacey_label6=Label(root,text="",bg="#c6e22d").grid(row=13,columnspan=5)#exit button
close_main_gui=Button(root,text="Exit",command=root.quit).grid(row=14,column=2)
spacey_label7=Label(root,text="",bg="#c6e22d").grid(row=15,columnspan=5)
root.mainloop()