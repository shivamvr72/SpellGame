from tkinter import*
import random
from english_words import get_english_words_set
from pygame import mixer
from tkinter import messagebox


mixer.init()

web2lower = get_english_words_set(['web2'], lower=True)

root = Tk()

# word counter 
n = 0
# shuffle counter
shuffle_count = 4
# score counter
score = 0

# inserting words into display
def ins(event=None):
    global score
    global n
    ps = web2lower
    
   
    
    if des.get() in ps:
        if des.get() in lbox.get(1.0, "end-1c"):
            pass
        else:
            
            # score updation logic
            if n > 10:
                score += 2
            else:
                score += 1
            
            # couter for no of words    
            n += 1
            
            # for level up
            if n == 10:
                messagebox.showinfo("Level 2", "Congratulation, Level Up!\n")
                global shuffle_count
                shuffle_count += 1
            Label(root, text=shuffle_count, fg="white", bg="blue", font="mosarrate 14 bold").place(x=420, y=30)
                
                
            lbox.insert(INSERT,f"{n}. {des.get()}\n")
            des.set("")
            mixer.music.load("./sound_adds.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            while mixer.music.get_busy():
                pass
            Label(root, text=score, fg="white", bg="blue", font="mosarrate 14 bold").place(x=610, y=30)
            
            
#====structure=======
lb1 = Label(root,text="Welcome to Spell", fg="white", bg="blue", font="mosarrate 14 bold")
lb1.place(x=40, y=30)


Label(root, text="Score:", fg="white", bg="blue", font="mosarrate 14 bold").place(x=540, y=30)
Label(root, text=score, fg="white", bg="blue", font="mosarrate 14 bold").place(x=610, y=30)

Label(root, text="Shuffle:", fg="white", bg="blue", font="mosarrate 14 bold").place(x=340, y=30)
Label(root, text="3", fg="white", bg="blue", font="mosarrate 14 bold").place(x=420, y=30)



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


# random character generator
def random_char_generator():
    return random_char[random.randint(0,len(random_char2)-1)]

# checking wheather the game is over or not game over
def game_over_check():
    global shuffle_count
    global score
    global n
    if shuffle_count <= 0:
        game_over_msg = messagebox.askokcancel("Game Over", "Game Over\nShuffle Finished\nDo You Want Play Again")
        if game_over_msg == False:
            exit()
        
        # to re assinging the value to restart
        lbox.delete("1.0","end")
        shuffle_count = 3
        score = 0
        n = 0
        Label(root, text=n, fg="white", bg="blue", font="mosarrate 14 bold").place(x=610, y=30)
        

# random button generator, assinger and binder
def rnd(event=None):
    
    global shuffle_count
    
    # game over 
    game_over_check()

    #updating and displaying suffle count
    shuffle_count -= 1
    Label(root, text=shuffle_count, fg="white", bg="blue", font="mosarrate 14 bold").place(x=420, y=30)
    des.set("")

    random_chars = [random_char_generator() for _ in range(10)]
    buttons = []

    for i, char in enumerate(random_chars):
        x = 40 + i * 60
        button = Button(root, text=char, width=2, fg="white", bg="blue", font="mosarrate 23 bold", command=lambda c=char: des.set(f"{des.get()}{c}"))
        button.place(x=x, y=360)
        buttons.append(button)

    for char in random_char:
        root.unbind(char)

    for i, char in enumerate(random_chars):
        root.bind(char, lambda event=None, c=char: des.set(f"{des.get()}{c}"))


    
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
    
    
btn_backspace = Button(root, text="Back Space", bg="white", fg="blue", width=9, font="mosarrate 20 bold", command=clr)
btn_backspace.place(x=470, y=450)
btn_shuffle = Button(root, text="Shuffle", bg="white", fg="blue", width=9, font="mosarrate 20 bold", command=rnd)
btn_shuffle.place(x=255, y=450)

Label(root, text="Powred by python", fg="white", bg="blue", font="mosarrate 10 bold").place(x=500, y=550)

#=====main window====
root.geometry("670x600+100+50")
root.resizable(0,0)
root.title("Spell")
root.config(bg= "Blue")
root.mainloop()