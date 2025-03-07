import tkinter as tk
import datetime

class ExaminationClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x150")
        self.root.title(" ")
        self.root.configure(bg="white")
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_rowconfigure(1,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_rowconfigure(2,weight=1)
        self.root.grid_columnconfigure(2,weight=1)
        
        self.current_date = tk.Label(self.root,bg="white",fg="black",text=(datetime.date.today()).strftime("%d/%m/%Y"),font=("Arial",25,"bold"))
        self.current_date.place(x=10,y=10)
        currtime = datetime.datetime.now()
        currtime = currtime.strftime('%H:%M:%S')
        self.time_label = tk.Label(self.root,fg="black",bg="white",text=currtime,font=("Arial",55,"bold"))
        self.time_label.pack(expand=True)
        self.CreateCurrentTimeScreen()
        
        self.root.mainloop()

    def CreateCurrentTimeScreen(self):
        currtime = datetime.datetime.now()
        currtime = currtime.strftime('%H:%M:%S')
        self.time_label.config(text=currtime)
        self.root.after(1000,self.CreateCurrentTimeScreen)
                
if __name__ == "__main__":
    ExaminationClock()
