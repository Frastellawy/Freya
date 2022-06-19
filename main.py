import tkinter as tk
import tkinter.ttk as ttk
import GUI
import os
import time
import requests
from threading import Thread
from zipfile import ZipFile
import shutil
import PIL
from PIL import Image

#####-------------------------------------------------------#####
#####----------------------- Threads -----------------------#####
#####-------------------------------------------------------#####
def download_Thread():
    app.listbox.write("Freya: Downloading Files.")
    app.listbox.write("Loading...")
    app.listbox.write("")
    app.listbox.write("*WARNING* Wait for completing all the download threads!")
    app.listbox.write("")


    app.module1.off()
    app.module2.off()
    app.module3.off()
    
    downloading = Thread(target = Download)
    downloading.start()
    #print(test)

def unzip_Thread():
    app.listbox.write("Freya: Unpacking Files.")
    app.listbox.write("Loading...")
    app.listbox.write("")
    app.listbox.write("*WARNING* Wait for completing all the unpack threads!")
    app.listbox.write("")

    app.module1.off()
    app.module2.off()
    app.module3.off()

    unzip = Thread(target = Unzip)
    unzip.start()

def convert_Thread():
    app.listbox.write("Freya: Converting Files.")
    app.listbox.write("Loading...")
    app.listbox.write("")
    app.listbox.write("*WARNING* Wait for completing all the convert threads!")
    app.listbox.write("")

    app.module1.off()
    app.module2.off()
    app.module3.off()

    unzip = Thread(target = Convert)
    unzip.start()

#####-------------------------------------------------------#####
#####-------------------------------------------------------#####
#####-------------------------------------------------------#####

def Download():
    urls = open("urls.txt", "r")
    content = urls.read()
    content_list = content.splitlines()
    urls.close()

    app.listbox.write(("Files to download: "+str(len(content_list))))
    app.listbox.write("Preparing...")
    app.listbox.write("")

    name = "File"
    for i in range(len(content_list)):
        fileinfo = "Downloading file: "+str(i+1)+" of "+str(len(content_list))
        app.listbox.write(fileinfo)

        r = requests.get(content_list[i])
        file_name = mdpath+"/"+name+str(i+1)+".zip"

        with open(file_name, "wb") as code:
            code.write(r.content)
            
        app.listbox.write("Completed.")
        time.sleep(2)
    
    app.listbox.write("Files succesfully downloaded!")
    app.listbox.write("")

    app.module1.on()
    app.module2.on()
    app.module3.on()


def Unzip():
    def removeFiles():
        app.listbox.write("Removing .zip files...")
        for file in files:
            os.remove(mdpath+"/"+file)
        app.listbox.write("Done!")
        app.listbox.write("")
        
    files = os.listdir(mdpath)
    #print(files)

    app.listbox.write("Preparing for unpacking files...")

    for file in files:
        file1 = mdpath+"/"+file
        name0 = file.split(".")
        name = mupath+"/"+name0[0]

        with ZipFile(file1, "r") as zip:
            app.listbox.write("Unpacking...")
            zip.extractall(name)

    app.listbox.write("All files succesfully unpacked!")
    app.listbox.write("")

    choicewindow = GUI.Window(app, "250x50", "Settings")
    frame = GUI.Frame(choicewindow, 0,0,300,100,0, "#e4eff7")
    frame.pack(fill=tk.BOTH)
    label = GUI.Label(frame, "Do you want to remove all .zip files?",\
                      "Arial", 11, "#e4eff7", "black", tk.TOP, False, tk.X)
    yesbtn = GUI.Button(frame, "Yes", 5, 5, tk.LEFT, True, None)
    nobtn =  GUI.Button(frame, "No", 5, 5, tk.LEFT, True, None)

    yesbtn.config(command=removeFiles)
    nobtn.config(command=choicewindow.destroy)

    app.module1.on()
    app.module2.on()
    app.module3.on()

def Convert():
    def c():
        app.listbox.write("Looking for files...")
        type1 = btype.get()
        type2 = atype.get()

        for root, dirs, files in os.walk(mcpath):
            for file in files:
                if file.endswith(type1):
                    h1_spl = file.split(".")
                    #print(h1_spl)
                    imgpath = root+"/"+file
                    img = Image.open(imgpath)
                    name = os.path.splitext(str(file))
                    #print(name)
                    savename = name[0]+type2
                    savepath = mcpath+"/"+savename
                    cinfo = "Converting "+str(file)+" into "+str(savename)
                    app.listbox.write(cinfo)
                    img.save(savepath)

        app.listbox.write("All files converted succesfully!")
        app.listbox.write("")
        
    
    app.listbox.write("Preparing for unpacking files...")
    
    window = GUI.Window(app, "300x200", "Settings")
    frame = GUI.Frame(window, 0,0,300,200,0, "#e4eff7")
    frame.pack(fill=tk.BOTH)
    label = GUI.Label(frame, "What type of file do you want to convert?",\
                      "Arial", 11, "#e4eff7", "black", tk.TOP, False, tk.X)
    label = GUI.Label(frame, "e.g.  .tiff",\
                      "Arial", 11, "#e4eff7", "grey", tk.TOP, False, tk.X)
    btype = GUI.Entry(frame, tk.TOP, True, None)
    label = GUI.Label(frame, "What type of file do you want to convert into?",\
                      "Arial", 11, "#e4eff7", "black", tk.TOP, False, tk.X)
    label = GUI.Label(frame, "e.g.  .jpg",\
                      "Arial", 11, "#e4eff7", "grey", tk.TOP, False, tk.X)
    atype = GUI.Entry(frame, tk.TOP, True, None)
    
    bokbtn = GUI.Button(frame, "Ok", 3, 1, tk.BOTTOM, True, None)

    

    bokbtn.config(command=c)
        

app = GUI.Freya()

app.listbox.write(app.fullname)
app.listbox.write("")
app.listbox.write("Welcome!")
app.listbox.write("Freya is an app for downloading files from https://finder.creodias.eu website.")
app.listbox.write("However she also has some other cool features.")
app.listbox.write("For a quick tutorial please open Tutorial.")
app.listbox.write("")
app.listbox.write("")

mpaths_read = open("paths.txt", "r")
mpaths = mpaths_read.read().splitlines()

mdpath = mpaths[0]
mupath = mpaths[1]
mcpath = mpaths[2]

app.module1.config(command=download_Thread)
app.module2.config(command=unzip_Thread)
app.module3.config(command=convert_Thread)

app.start()
