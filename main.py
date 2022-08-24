import tkinter.messagebox
from tkinter import *

# => Create our window with customize size
root = Tk()
root.geometry("1350x750+0+0")
root.title("Arshiya Tic Tac Toe")
root.configure(background='Cadet Blue')

# =>   manage organises widgets in a table-like structure in the parent widget
Tops = Frame(root,bg ='Cadet Blue',pady = 2 , width=1350,height=100,relief=RIDGE)
Tops.grid(row=0,column=0)


# => we create our lable on window
labelTitle = Label(Tops,font=('arial',50,'bold'), text = "Arshiya's Tic Tac Toe Game" , bd = 21 , bg = 'Cadet Blue' , fg = 'Cornsilk',justify=CENTER)
labelTitle.grid(row=0,column=0)


# => we create main or middle of window
MainFrame = Frame(root,bg ='Powder Blue',pady = 2 , width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1,column=0)


# => left frame
leftFrame = Frame(MainFrame , bd = 10 , width=750 , height=500, pady=2,padx = 10,bg='Cadet Blue',relief=RIDGE)
leftFrame.pack(side=LEFT)


# => right frame
rightFrame = Frame(MainFrame,bd=10,width=560,height=200,padx=10,pady=2,bg='Cadet Blue' , relief=RIDGE)
rightFrame.pack(side=RIGHT)


# => second right frame
rightFrame1 = Frame(rightFrame,bd=10,width=560,height=200,padx=10,pady=2,bg='Cadet Blue' , relief=RIDGE)
rightFrame1.grid(row = 0 , column=0)


# => third right frame
rightFrame2 = Frame(rightFrame,bd=10,width=560,height=200,padx=10,pady=2,bg='Cadet Blue' , relief=RIDGE)
rightFrame2.grid(row = 1 , column=0)


# => create our play
playerX = IntVar()
playerO = IntVar()

# => set value
playerX.set(0)
playerO.set(0)


button = StringVar()
click= True


# crate function to check button for X and o
def check(buttons):
    global click
    if buttons['text'] == ' ' and click == True:
        buttons ['text'] = 'X'
        click = False
        givePoint()
    elif buttons['text'] == ' ' and click ==False:
        buttons['text'] = 'O'
        click = True
        givePoint()

""" give point to players       """
def givePoint():
    if ((button1)['text'] =='X') and \
        (button2['text']=='X')and \
        (button3['text']=='X'):
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player','you won a game')

    if ((button4)['text'] == 'X') and \
            (button5['text'] == 'X') and \
            (button6['text'] == 'X'):
        button4.configure(background='Yellow')
        button5.configure(background='Yellow')
        button6.configure(background='Yellow')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player', 'you won a game')

    if ((button7)['text'] == 'X') and \
            (button8['text'] == 'X') and \
            (button9['text'] == 'X'):
        button7.configure(background='Red')
        button8.configure(background='Red')
        button9.configure(background='Red')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player', 'you won a game')

    if ((button1)['text'] == 'X') and \
            (button4['text'] == 'X') and \
            (button7['text'] == 'X'):
        button1.configure(background='Pink')
        button4.configure(background='Pink')
        button7.configure(background='Pink')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player', 'you won a game happy mappy')

    if ((button2)['text'] == 'X') and \
            (button5['text'] == 'X') and \
            (button8['text'] == 'X'):
        button2.configure(background='Green')
        button5.configure(background='Green')
        button8.configure(background='Green')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player', 'you won a game')

    if ((button3)['text'] == 'X') and \
            (button6['text'] == 'X') and \
            (button9['text'] == 'X'):
        button3.configure(background='Purple')
        button6.configure(background='Purple')
        button9.configure(background='Purple')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player', 'you won a game')

    if ((button1)['text'] == 'X') and \
            (button5['text'] == 'X') and \
            (button9['text'] == 'X'):
        button1.configure(background='Blue')
        button5.configure(background='Blue')
        button9.configure(background='Blue')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player', 'you won a game')

    if ((button3)['text'] == 'X') and \
            (button5['text'] == 'X') and \
            (button7['text'] == 'X'):
        button3.configure(background='Blue')
        button5.configure(background='Blue')
        button7.configure(background='Blue')
        x = float(playerX.get())
        score = (x + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo('Winner X player', 'you won a game')

    """ now for PLayer O"""
    if ((button1)['text'] == 'O') and \
            (button2['text'] == 'O') and \
            (button3['text'] == 'O'):
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')

    if ((button4)['text'] == 'O') and \
            (button5['text'] == 'O') and \
            (button6['text'] == 'O'):
        button4.configure(background='Orange')
        button5.configure(background='Orange')
        button6.configure(background='Orange')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')

    if ((button7)['text'] == 'O') and \
            (button8['text'] == 'O') and \
            (button9['text'] == 'O'):
        button7.configure(background='Red')
        button8.configure(background='Red')
        button9.configure(background='Red')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')

    if ((button1)['text'] == 'O') and \
            (button4['text'] == 'O') and \
            (button7['text'] == 'O'):
        button1.configure(background='Pink')
        button4.configure(background='Pink')
        button7.configure(background='Pink')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')

    if ((button2)['text'] == 'O') and \
            (button5['text'] == 'O') and \
            (button8['text'] == 'O'):
        button2.configure(background='Green')
        button5.configure(background='Green')
        button8.configure(background='Green')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')

    if ((button3)['text'] == 'O') and \
            (button6['text'] == 'O') and \
            (button9['text'] == 'O'):
        button3.configure(background='Purple')
        button6.configure(background='Purple')
        button9.configure(background='Purple')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')

    if ((button1)['text'] == 'O') and \
            (button5['text'] == 'O') and \
            (button9['text'] == 'O'):
        button1.configure(background='Blue')
        button5.configure(background='Blue')
        button9.configure(background='Blue')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')

    if ((button3)['text'] == 'O') and \
            (button5['text'] == 'O') and \
            (button7['text'] == 'O'):
        button3.configure(background='Blue')
        button5.configure(background='Blue')
        button7.configure(background='Blue')
        x = float(playerO.get())
        score = (x + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo('Winner O player', 'you won a game')


"""                             """




"""         Reset function      """
def reset():
    button1['text']=' '
    button2['text']=' '
    button3['text']=' '
    button4['text']=' '
    button5['text']=' '
    button6['text']=' '
    button7['text']=' '
    button8['text']=' '
    button9['text']=' '

    # => change background of buttons

    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')
"""                             """


""" New Game function"""
def NewGame():
    reset()
    playerX.set(0)
    playerO.set(0)
"""                  """

labelX= Label(rightFrame1,font=('arial',40,'bold'),text="Player  X :" , padx=2,pady=2,bg = 'Cadet Blue' )
labelX.grid(row=0,column=0,sticky=W)
txtPlayerX = Entry(rightFrame1,font=('arial',40,'bold'),bd = 2,fg = 'black',textvariable=playerX,width=14,
                   justify=LEFT).grid(row=0,column=1)


labelO = Label(rightFrame1,font=('arial',40,'bold'),text="Player  O :" ,padx=2,pady=2 , bg = 'Cadet Blue' )
labelO.grid(row=1,column=0,sticky=W)
txtPlayerO = Entry(rightFrame1,font=('arial',40,'bold'),bd = 2,fg = 'black',textvariable=playerO,width=14,
                   justify=LEFT).grid(row=1,column=1)

# => create reset button and new game
btnReset = Button(rightFrame2,text="Reset ",font=('arial',40,'bold'),height=1,width=20,bg='gainsboro',command=reset)
btnReset.grid(row=0,column=0,padx=6,pady=11)

btnNewGame = Button(rightFrame2,text="New Game ",font=('arial',40,'bold'),height=1,width=20,bg='gainsboro',command=NewGame)
btnNewGame.grid(row=1,column=0,padx=6,pady=11)



# => Create our buttons for playing game
button1 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 = Button(leftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda :check(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)



root.mainloop()
