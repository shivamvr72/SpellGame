from tkinter import*
import random
from english_words import get_english_words_set
from pygame import mixer

mixer.init()

web2lower = get_english_words_set(['web2'], lower=True)

root = Tk()
n = 0
def ins(event=None):
    # es = ent.insert(INSERT, des.get())
    # ps = ['AS', 'SINE', 'SEE', 'KITE', 'JOY', 'JUST',"AWAKE", 'DO', 'RUN', 'GO', 'LOVE', 'LIKE', 'HURRY', 'SPEED', 'SLOW', 'SMELL', 'JOIN', 'AFTER', 'ALL', 'AN', 'ANT', 'AXE', 'ALIKE', 'ASK', 'CONFESS', 'ROLL', 'RISE', 'ROWER', 'MAN', 'LAUGH', 'PEASE', 'PIECE', 'PICS', 'PICTURES','POSE','ROSE','REEL','REAL','RACE','CASTE','CASTLE']
    
    ps = web2lower
    
    if des.get() in ps:
        if des.get() in lbox.get(1.0, "end-1c"):
            pass
        else:
            global n
            n += 1
            lbox.insert(INSERT,f"{n}. {des.get()}\n")
            des.set("")
            mixer.music.load("./sound_adds.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            while mixer.music.get_busy():
                pass
            
#====structure=======
lb1 = Label(root,text="Welcome to Spell", fg="white", bg="blue", font="mosarrate 14 bold")
lb1.place(x=40, y=30)

lbox = Text(root, height=10, width=54, fg="blue", bg="white", font="mosarrate 14 bold")
lbox.place(x=40, y=70)

des = StringVar()
ent = Entry(root, width=37, textvariable=des, fg="blue", bg="white", font="mosarrate 21 bold")
ent.place(x=40, y=310)

random_char2 = ['A','A','A', 'B', 'C', 'D', 'E', 'E', 'F', 'G', 'H', 'I','I', 'J', 'K', 'L', 'M', 'N', 'O','O', 'P', 'Q', 'R', 'S','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#[chr(i) for i in range(65,91)]S
random_char = []
for j in random_char2:
    random_char.append(j.lower())

randoms = []

    
    
def rnd(event=None):
    des.set("")     
    
    r1=random_char[random.randint(0,len(random_char)-1)]
    r2=random_char[random.randint(0,len(random_char)-1)]
    r3=random_char[random.randint(0,len(random_char)-1)]
    r4=random_char[random.randint(0,len(random_char)-1)]
    r5=random_char[random.randint(0,len(random_char)-1)]
    r6=random_char[random.randint(0,len(random_char)-1)]
    r7=random_char[random.randint(0,len(random_char)-1)]
    r8=random_char[random.randint(0,len(random_char)-1)]
    r9=random_char[random.randint(0,len(random_char)-1)]
    r10=random_char[random.randint(0,len(random_char)-1)]


    le1 = Button(root,text=r1, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r1}"))
    le1.place(x=40, y=360)
    le2 = Button(root,text=r2, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r2}"))
    le2.place(x=100, y=360)
    le3 = Button(root,text=r3, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r3}"))
    le3.place(x=160, y=360)
    le4 = Button(root,text=r4, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r4}"))
    le4.place(x=220, y=360)
    le5 = Button(root,text=r5, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r5}"))
    le5.place(x=280, y=360)
    le6 = Button(root,text=r6, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r6}"))
    le6.place(x=340, y=360)
    le7 = Button(root,text=r7, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r7}"))
    le7.place(x=400, y=360)
    le8 = Button(root,text=r8, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r8}"))
    le8.place(x=460, y=360)
    le9 = Button(root,text=r9, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r9}"))
    le9.place(x=520, y=360)
    le10 = Button(root,text=r10, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda:des.set(f"{des.get()}{r10}"))
    le10.place(x=580, y=360)

    
    
    root.bind(r1, lambda event=None:des.set(f"{des.get()}{r1}"))
    root.bind(r2, lambda event=None:des.set(f"{des.get()}{r2}"))
    root.bind(r3, lambda event=None:des.set(f"{des.get()}{r3}"))
    root.bind(r4, lambda event=None:des.set(f"{des.get()}{r4}"))
    root.bind(r5, lambda event=None:des.set(f"{des.get()}{r5}"))
    root.bind(r6, lambda event=None:des.set(f"{des.get()}{r6}"))
    root.bind(r7, lambda event=None:des.set(f"{des.get()}{r7}"))
    root.bind(r8, lambda event=None:des.set(f"{des.get()}{r8}"))
    root.bind(r9, lambda event=None:des.set(f"{des.get()}{r9}"))
    root.bind(r10, lambda event=None:des.set(f"{des.get()}{r10}"))

    
    root.bind("<Button-1>", lambda event=None:root.focus_force())
    # =================================
    
    mixer.music.load("./sound_spells.wav")
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while mixer.music.get_busy():
        pass

root.bind("<BackSpace>", lambda event=None:des.set(f"{des.get()[:-1]}"))
root.bind("<Button-1>", lambda event=None:root.focus_force())
root.bind("<space>", rnd)
btn1 = Button(root, text="Spell", bg="white", fg="blue", width=9, font="mosarrate 20 bold", command=ins)
btn1.place(x=40, y=450)
root.bind("<Return>", ins)

def clr():
    des.set(f"{des.get()[:-1]}")
btn2 = Button(root, text="Back Space", bg="white", fg="blue", width=9, font="mosarrate 20 bold", command=clr)
btn2.place(x=470, y=450)
btn3 = Button(root, text="Suffle", bg="white", fg="blue", width=9, font="mosarrate 20 bold", command=rnd)
btn3.place(x=255, y=450)

#=====main window====
root.geometry("670x600")
root.resizable(0,0)
root.title("Spell")
root.config(bg= "Blue")
root.mainloop()