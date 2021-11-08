import tkinter as tk
from tkinter import Frame, filedialog
from tkinter import font
from tkinter.constants import CENTER

#on click listener for open file button
def open_a_file():

    video_formats = ".mp4 .mkv .mov"    # we can add more video formats here
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
                filetypes= [("Video", video_formats)])
    
    labelfont = font.Font(family='Arial', size=12, weight='bold') # label font
    label = tk.Label(text=filename,bg="white",font=labelfont, wraplength=400,
                   justify="left")
    label.place(relx=0.5,rely=0.2,anchor=CENTER)
                


#Initialising Main Window of the application
window = tk.Tk()
window.title("Human Detecting System")
window.geometry("500x500")

#Initialising font for buttons
buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

#Initialising open file button
openFile = tk.Button(window,text="Open File",padx=10,pady=5,
                    fg="white",bg="#263D42",font=buttonFont,command=open_a_file)
openFile.place(relx=0.5, rely=0.4, anchor=CENTER)

#Initialising process the file button
process = tk.Button(window,text="Process",padx=10,pady=5,
                    fg="white",bg="#263D42",font=buttonFont)
process.place(relx=0.5, rely=0.6, anchor=CENTER)


window.mainloop()
