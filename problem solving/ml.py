import tkinter as tk
from tkinter import filedialog
r = tk.Tk() 
r.title('Counting Seconds')
def fd():
    global filename
    filename=filedialog.askopenfilename(initialdir = "/",title = "Select file")
    

button = tk.Button(r, text='Browse', width=15, command=fd)
print(filename)
button.pack() 
r.mainloop()


#button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
