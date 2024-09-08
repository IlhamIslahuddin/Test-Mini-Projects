import tkinter as tk

window = tk.Tk()

window.geometry("1000x800")
#sets size of window

window.title("Tkinter Window")
#sets title of window

label = tk.Label(window, text="Hello World", font=('Arial',18))
label.pack(padx=20, pady=20)
#format

textbox = tk.Text(window, height= 3, font=('Arial',16))
textbox.pack(padx=20)

entry = tk.Entry(window)
#single line textbox/height 1
entry.pack(pady=10)

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
#frame for buttons

btn1 = tk.Button(buttonframe, text="1", font= ('Arial',18))
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font= ('Arial',18))
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font= ('Arial',18))
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font= ('Arial',18))
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font= ('Arial',18))
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font= ('Arial',18))
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')
#pack is the general format 

button = tk.Button(window, text="I am a button.", font=('Arial',18))
button.pack(pady=10)

anotherbtn = tk.Button(window, text="I can be anywhere")
anotherbtn.place(x=200, y=200, height=100, width=100)
#set in a location without formatting

window.mainloop()
