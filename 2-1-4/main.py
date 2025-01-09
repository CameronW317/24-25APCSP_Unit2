#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

frame_login = tk.Frame(root)

#Activate the grid in our new frame
frame_login.grid()

#Widget for frame login

lbl_username = tk.Label(frame_login, text='Username: ', fg = 'red', font = 'Times 16')
lbl_username.pack(padx = 50, pady = 50)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

root.mainloop()