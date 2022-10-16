import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import *
from turtle import bgcolor
from transum import summarizer

#from spacy_summarization import text_summarizer
#from nltk_summarization import nltk_summarizer

def clrorg():
    orgtxt.delete(1.0,END)

def clrsum():
    sumtxt.delete(1.0,END)
    

def fileopen():
    try:
        file = filedialog.askopenfilename(title="Text Document",filetypes=(("Text file","*.txt"),("All files","*.*")))
        file = open(file,'r')
        r = file.read()
        clrorg()
        orgtxt.insert(END,r)
        file.close()
    except:
        pass


def openFile():
    txt = orgtxt.get(1.0,END)
    if txt == '\n':
        fileopen()
    else:
        ans = messagebox.askyesnocancel('Warning','Textbox not empty, Do you want to overwrite!!!')
        if ans == True:
            fileopen()


def summ(txt):
    res = summarizer(txt)
    clrsum()
    sumtxt.insert(END,res)

def summary():
    txt = orgtxt.get(1.0,END)
    if txt == '\n':
        messagebox.showerror('Error', 'No Text to Summarize!!!')
    else:
        stxt = sumtxt.get(1.0,END)
        if stxt == '\n':
            summ(txt)
        else:
            ans = messagebox.askyesnocancel('Warning','Textbox not empty, Do you want to overwrite!!!')
            if ans == True:
                summ(txt)
    

def saveFile():
    txt = orgtxt.get(1.0,END)
    if txt == '\n':
        messagebox.showerror('Error', 'No Summarized Text!!!')
    else:
        try:
            file = filedialog.asksaveasfile(title="Text Document", defaultextension='.txt',filetypes=[
            ("Text file",".txt"),
            ("Doc file",".doc"),
            ("HTML file",".html"),
            ("All files","*.*")
            ])
            file.write(sumtxt.get(1.0,END))
            file.close()
            messagebox.showinfo("Information","Text Saved Successfully!!!")
        except:
            pass

def clrorgtxt():
    txt = orgtxt.get(1.0,END)
    if txt != '\n':
        ans = messagebox.askyesnocancel('Warning','Textbox not empty, Do you want to clear all the text!!!')
        if ans == True:
            clrorg()     


def clrsumtxt():
    txt = sumtxt.get(1.0,END)
    if txt != '\n':
        ans = messagebox.askyesnocancel('Warning','Textbox not empty, Do you want to clear all the text!!!')
        if ans == True:
            clrsum() 
    


window = Tk()
window.title('Text Summarizer App')
window.geometry('1330x550')

tabctrl = ttk.Notebook(window)

hometab = ttk.Frame(tabctrl)
filetab = ttk.Frame(tabctrl)
onlinetab = ttk.Frame(tabctrl)
algorithmtab = ttk.Frame(tabctrl)
abouttab = ttk.Frame(tabctrl)

tabctrl.add(hometab,text=f' {"Home":^10s}')
tabctrl.add(filetab,text=f' {"File":^10s}')
tabctrl.add(onlinetab,text=f' {"Online":^10s}')
tabctrl.add(algorithmtab,text=f' {"Algorithm":^10s}')
tabctrl.add(abouttab,text=f' {"About":^10s}')

tabctrl.pack(expand=1,fill='both')

orglbl = Label(hometab,text='Text to Summarize:',font="ar 12 bold")
orglbl.grid(column=0,row=0)
orgtxt = ScrolledText(hometab,height=20)
orgtxt.grid(row=1, column=0)

opnbtn = Button(hometab,text="Open Text Document",fg='blue', width=20, command=openFile)
opnbtn.grid(row=2, column=0)

clrorgbtn = Button(hometab,text="Clear Text",fg='red', width=20, command=clrorgtxt)
clrorgbtn.grid(row=3, column=0)

sumbtn = Button(hometab, text="Summarize Text",fg='green', width=20, command=summary)
sumbtn.grid(row=4, column=0)


sumlbl = Label(hometab, text="Summarized Text:", font="ar 12 bold")
sumlbl.grid(row=0, column=1)
sumtxt = ScrolledText(hometab,height=20)
sumtxt.grid(row=1, column=1)

savebtn = Button(hometab,text="Save Summarized Text",fg='green', width=20, command=saveFile)
savebtn.grid(row=2, column=1)

clrsumbtn = Button(hometab, text="Clear Text",fg='red', width=20, command=clrsumtxt)
clrsumbtn.grid(row=3, column=1)



window.mainloop()