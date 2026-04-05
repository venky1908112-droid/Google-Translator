from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text = "type", src = "english", dest = "hindi"):
    text1 = text
    src1 = src
    dest1  = dest
    trans = Translator()
    trans1 = trans.translate(text1,src = src1,dest = dest1)
    return trans1.text

def data():
    s = combo_src.get()
    d = combo_dest.get()
    msg = source_text.get(1.0,END)
    textget = change(text = msg,src = s, dest = d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)


root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg ="RED")

lab_txt = Label(root, text = "TRANSLATOR", font = ("Time New Roman", 20, "bold"))
lab_txt.place(x = 100, y = 40, height = 50, width = 300)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root, text = "Source Text", font = ("Time New Roman", 20, "bold"),fg = "black",bg = "red")
lab_txt.place(x = 100, y = 100,height = 20, width = 300)

source_text = Text(frame,font = ("Time New Roman", 20, "bold"),wrap = WORD)
source_text.place(x = 10, y = 130, height = 150, width = 480)

list_text = list(LANGUAGES.values())

combo_src = ttk.Combobox(frame, value = list_text)
combo_src.place(x = 10, y = 300, height = 40, width = 100)
combo_src.set("English")

button_change = Button(frame, text = "Translate",relief = RAISED,command = data)
button_change.place(x = 200, y = 300, height = 40, width = 100)

combo_dest = ttk.Combobox(frame, value = list_text)
combo_dest.place(x = 390, y = 300, height = 40, width = 100)
combo_dest.set("English")

lab_txt = Label(root, text = "Dest Text", font = ("Time New Roman", 20, "bold"),bg = "red")
lab_txt.place(x = 100, y = 370,height = 20, width = 300)

dest_text = Text(frame,font = ("Time New Roman", 20, "bold"),wrap = WORD)
dest_text.place(x = 10, y = 400, height = 150, width = 480)



root.mainloop()