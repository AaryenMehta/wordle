import tkinter as tk
import random
import time
from turtle import bgcolor

word = ''

def create_grid(event=None):
    w = c.winfo_width()
    h = c.winfo_height() 
    c.delete('grid_line') 

    for i in range(0, w, 200):
        c.create_line([(i, 0), (i, h)], tag='grid_line', fill="#3E3E40", width="15")

    for i in range(0, h, 160):
        c.create_line([(0, i), (w, i)], tag='grid_line', fill="#3E3E40", width="15")

def process(event=None):

    global word, answer, i, used
    temp = answer

    i += 1

    content = user_name.get() # get the contents of the entry widget
    user_name.delete(0,tk.END)
    word = content

    if i < 6 :
        word = word.lower()
        if word not in allowed or word in used:
            i -= 1
            return 
        if i == 5:
            print(answer)

        word = word.upper()
        used.append(word)
        green = "#578C4F"
        black = "#0C0B0D"
        yellow = "#BF9F3F"

        xd = [0]*5
        for j in range(5):
            if word[j] == answer[j]:
                xd[j] = green
                temp = temp[:j]+"0"+temp[j+1:]

        temp2 = ''

        for k in range(len(temp)):
            if temp[k] != "0":
                temp2 += temp[k]

        temp = temp2

        for j in range(5):
            if word[j] in temp and xd[j] == 0:
                xd[j] = yellow
            elif word[j] not in temp:
                if xd[j] == 0:
                    xd[j] = black

        for j in range(5):
            r = c.create_rectangle(200*j,160*i,200*(j+1),160*(i+1),fill=xd[j],outline="#3E3E40",width="15")
            c.create_text(100+200*j,90+160*i,text=word[j],font=("Helvetica 70 bold"),fill="#D2D6D9")
            root.update()
            root.after(800)

root = tk.Tk()
used = []
root.title("Wordle")
c = tk.Canvas(root, height=960, width=1000, bg='#0C0B0D')
c.pack(fill=tk.BOTH, expand=True)
c.bind('<Configure>', create_grid)

with open('input.txt') as f:
    possible = [line.rstrip('\n') for line in f]

with open('allowed_words.txt') as f:
    allowed = [line.rstrip('\n') for line in f]
    
answer = random.choice(possible)
answer = answer.upper()

var = tk.StringVar()
user_name = tk.Entry(root,textvariable=var)
user_name.pack()
user_name.bind('<Return>',process)

i = -1  
root.mainloop()