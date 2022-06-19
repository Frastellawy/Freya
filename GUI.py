import tkinter as tk
import tkinter.ttk as ttk
import importlib
import os
import time

'''###---------------------------------------------------######
######---------------------------------------------------######
######---------------------------------------------------###'''

name = "Freya"
version = "1.0"

'''###---------------------------------------------------######
######---------------------------------------------------######
######---------------------------------------------------###'''

class Freya(tk.Tk):
    def __init__(self):
        super().__init__()
        self.fullname = name + "   v." + version
        self.title(self.fullname)
        self.geometry("1000x800")
        self.resizable(0,0)

        self.title_frame = Frame(self, 0,0,100,400,0, "#2a2a2a")
        self.button_frame = Frame(self, 0,100,700,400,0, "#e4eff7")
        self.main_frame = Frame(self, 400,0,800,600,0, "white")

        

        self.scrollbar = Scrollbar(self.main_frame, tk.RIGHT, tk.Y)
        self.listbox = Listbox(self.main_frame, self.scrollbar.set, 49, tk.TOP, tk.BOTH)

        self.mainmenu = Menu(self)
        self.mainmenu.add_command(label = "Tutorial")
        self.mainmenu.add_command(label = "Paths", command=self.paths_window)
        self.mainmenu.add_command(label = "Exit", command=self.destroy)

        self.config(menu=self.mainmenu)

        self.title_label = Label(self.title_frame, self.fullname, "Blackadder ITC", 30, "#2a2a2a","white",tk.TOP, True, tk.BOTH)

        self.module1 = Button(self.button_frame, "Downloading Files", 10, 5, tk.TOP, False, tk.X)
        self.module2 = Button(self.button_frame, "Unpacking Files", 10, 5, tk.TOP, False, tk.X)
        self.module3 = Button(self.button_frame, "Converting Files", 10, 5, tk.TOP, False, tk.X)
        
        ##################################################################
        ##################################################################
        ##################################################################

    def start(self):
        tk.mainloop()     

    def paths_window(self):
        def savepath():
            p01 = dentry.get()
            p02 = uentry.get()
            p03 = centry.get()

            p11 = p01.replace(os.sep,'/')
            p12 = p02.replace(os.sep,'/')
            p13 = p03.replace(os.sep,'/')
            
            lpaths = str(p11)+"\n"+str(p12)+"\n"+str(p13)

            f = open('paths.txt', 'w')
            f.write(lpaths)
            f.close()

            window.destroy()

        f = open('paths.txt', 'r')
        file = f.read()
        paths = file.split('\n')
        f.close()
            
        window = Window(self, "900x100", "Paths settings")
        window.grab_set()
        frame1 = Frame(window,0,0,100,150,0,"#e4eff7")
        frame2 = Frame(window,150,0,100,600,0,"#e4eff7")
        frame3 = Frame(window,750,0,100,150,0,"#e4eff7")

        dpath_label = Label(frame1, "Downloading Path", "Arial", 10, "#e4eff7", "black", tk.TOP, True, tk.X)
        upath_label = Label(frame1, "Unpacking Path", "Arial", 10, "#e4eff7", "black", tk.TOP, True, tk.X)
        cpath_label = Label(frame1, "Converting Path", "Arial", 10, "#e4eff7", "black", tk.TOP, True, tk.X)

        dentry = tk.Entry(frame2)
        uentry = tk.Entry(frame2)
        centry = tk.Entry(frame2)
        
        dentry.pack(side=tk.TOP,expand=True, fill=tk.X)
        uentry.pack(side=tk.TOP,expand=True, fill=tk.X)
        centry.pack(side=tk.TOP,expand=True, fill=tk.X)

        savebtn = Button(frame3, "Save", 10, 5, tk.TOP, True, tk.BOTH)
        savebtn.config(command=savepath)

        try:
            dentry.insert(0,paths[0])
        except IndexError:
            self.listbox.write("Downloading path is empty. Please, enter downloading path.")
            pass

        try:
            uentry.insert(0,paths[1])
        except IndexError:
            self.listbox.write("Unpacking path is empty. Please, enter downloading path.")
            pass
        
        try:
            centry.insert(0,paths[2])
        except IndexError:
            self.listbox.write("Converting path is empty. Please, enter downloading path.")
            pass

        
        

class Frame(tk.Frame):
    def __init__(self, x, posX, posY, height, width, p, bgr):
        super().__init__(x, height = height, width = width, bg = bgr)
        self.pack_propagate(p)
        self.place(x=posX, y=posY)


class Label(tk.Label):
    def __init__(self, x, text, font, fsize, bgr, fgr, sd, expd, fl):
        super().__init__(x, text = text, font = (font, fsize), bg = bgr, fg = fgr)
        self.pack(side=sd, expand=expd, fill=fl)

class Button(tk.Button):
    def __init__(self, x, text, width, height, sd, expd, fl):
        super().__init__(x, text = text, cursor = "plus",\
                         font = ("Arial", 12, "bold"),\
                         width = width, height = height, bd = 3,\
                         relief=tk.RAISED, fg="black", bg="#e4eff7",\
                         activeforeground="black", activebackground="#f7e4e4")
        self.pack(side=sd, expand=expd, fill=fl)
    def on(self):
        self["state"] = tk.NORMAL
    def off(self):
        self["state"] = tk.DISABLED


class Entry(tk.Entry):
    def __init__(self, x, sd, expd, fl):
        super().__init__(x)
        self.pack(side=sd, expand=expd, fill=fl)

class Scrollbar(tk.Scrollbar):
    def __init__(self, x, sd, fl):
        super().__init__(x)
        self.pack(side=sd, fill=fl)

class Listbox(tk.Listbox):
    def __init__(self, x, command, height, sd, fl):
        super().__init__(x, yscrollcommand = command, height = height)
        self.pack(side=sd, fill=fl)

    def write(self, text):
        self.insert(tk.END, text+"\n")

class Menu(tk.Menu):
    def __init__(self, x):
        super().__init__(x)

class Window(tk.Toplevel):
    def __init__(self, parent, geometry, title):
        super().__init__(parent)

        self.geometry(geometry)
        self.title(title)


