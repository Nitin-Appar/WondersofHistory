import tkinter as tk
import data_retrieve







def text_change():
    global text

    text=text+1

    if text >len(data_retrieve.eventlist):
        text = 0

    print("changed to colour number: ", text)

    
    btn.config(text=data_retrieve.eventlist[text])

def text_print():
    print("current colour number: ", text)



    
text=-1
root = tk.Tk()

btn = tk.Button(text="click to see colours", command=text_change, width=125, height=25)
btn.grid(row=1, column=1)

btn2 = tk.Button(text="console", command=text_print, width=10, height=3)
btn2.grid(row=2, column=1)

root.mainloop()

