from tkinter import Label, Tk, Text
import time
app_window = Tk()
app_window.title("Dijital Saat")
app_window.geometry("420x260")
app_window.resizable(1,1)
textWidget = Text(app_window)

text_font = ("Boulder", 68, 'bold')
background = "#000000"
foreground = "#ffffff"
border_width = 25

label = Label(app_window,
        font=text_font,
        bg=background,
        fg=foreground,
        bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%D\n%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()