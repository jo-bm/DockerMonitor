#!/usr/bin/env python3

import subprocess
from tkinter import *

sep = '-'*100

root = Tk()
root.geometry("1200x800")
root.configure(bg='#300A24')

def yes_no():
    response = subprocess.check_output("zenity --question --text='Are you sure you want to continue?'", shell=True)
    if response == b'':
        return "YES"
    else:
        return "NO"


def display_conts():
    result = subprocess.run(["docker", "ps", "-a"], stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")

    log['text'] = result
    root.after(1000, display_conts)

def rm_all_conts():
    result = subprocess.run(["docker", "ps", "-aq"], stdout=subprocess.PIPE)
    container_id = result.stdout.decode("utf-8").split()

    for conid in container_id:
        subprocess.run(["docker", "rm", "-f", conid], stdout=subprocess.PIPE)

def rm_only():
    # Get the text entered by the user
    text = entrycont.get()
    subprocess.run(["docker", "rm", "-f", text], stdout=subprocess.PIPE)


def display_imgs():
    result = subprocess.run(["docker", "images"], stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")

    log2['text'] = result
    root.after(1000, display_imgs)

def rm_all_img():
    result = subprocess.run(["docker", "images", "-q"], stdout=subprocess.PIPE)
    imgs = result.stdout.decode("utf-8").split()
    if yes_no() == "YES":
        print('You choose to delete all of your images')
    
        for img in imgs:

            subprocess.run(["docker", "image", "rm", "-f", img], stdout=subprocess.PIPE)
    else:
        print('No')

def print_imgs():
    result = subprocess.run(["docker", "images", "-q"], stdout=subprocess.PIPE)
    imgs = result.stdout.decode("utf-8")

    result = subprocess.run(["zenity", "--info", f"--text={imgs}"], stdout=subprocess.PIPE)

def rm_imgonly():
    # Get the text entered by the user
    text = entryimg.get()
    subprocess.run(["docker", "image", "rm", "-f", text], stdout=subprocess.PIPE)

def display_vols():
    result = subprocess.run(["docker", "volume","ls"], stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")

    log3['text'] = result
    root.after(1000, display_vols)


def rm_vols():
    result = subprocess.run(["docker", "volume", "ls","-q"], stdout=subprocess.PIPE)
    vols = result.stdout.decode("utf-8").split()
    if yes_no() == "YES":
        print('You choose to delete all of your vols')
    
        for vol in vols:

            subprocess.run(["docker", "volume", "rm", vol], stdout=subprocess.PIPE)
    else:
        print('No')

Label(text='Containers:',font="Ariel,30",bg='#300A24',fg='#3465A3').pack()
log = Label(text='abc',font="Ariel",bg='#300A24',fg='#3B6E07')
log.pack()

button = Button(root, text="rm all containers",font="Ariel,30",bg='#3465A3',fg='#000000', command=rm_all_conts)
button.pack()


button = Button(root, text="rm only",font="Ariel,30",bg='#3465A3',fg='#000000', command=rm_only)
button.pack()
entrycont = Entry(root)
entrycont.pack()

Label(text=f'{sep}',font="Ariel,30",bg='#300A24',fg='#3465A3').pack()


Label(text='\nImages:',font="Ariel,30",bg='#300A24',fg='#3465A3').pack()
log2 = Label(text='abc',font="Ariel",bg='#300A24',fg='#3B6E07')
log2.pack()

button = Button(root, text="rm all imgs",font="Ariel,30",bg='#3B6E07',fg='#000000', command=rm_all_img)
button.pack()
#button.place(x=70,y=130)

button = Button(root, text="rm only",font="Ariel,30",bg='#3B6E07',fg='#000000', command=rm_imgonly)
button.pack()

button = Button(root, text="print ids",font="Ariel,30",bg='#3B6E07',fg='#000000', command=print_imgs)
button.pack()

entryimg = Entry(root)
entryimg.pack()

Label(text=f'{sep}',font="Ariel,30",bg='#300A24',fg='#3465A3').pack()

Label(text='\nVolumes:',font="Ariel,30",bg='#300A24',fg='#3465A3').pack()
log3 = Label(text='abc',font="Ariel",bg='#300A24',fg='#3B6E07')
log3.pack()

button = Button(root, text="rm all vols",font="Ariel,30",bg='#3465A3',fg='#000000', command=rm_vols)
button.pack()





display_conts()
display_imgs()
display_vols()
root.mainloop()

