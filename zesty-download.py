from pytube import YouTube
import customtkinter
import os

panel = 0

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

vid =""
#main-GUI
app = customtkinter.CTk()
app.title("Zesty Download")
app.geometry("500x300")

def getV():
    if link.get() != "":
     
     ytLink = link.get()
     ytThing = YouTube(ytLink)

     screen = customtkinter.CTkToplevel(app)
     screen.title("Download")
     screen.geometry("500x300")

     

     resolution =[str(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in ytThing.streams if i.resolution])))]
     
     def select():
       global vid
       vid = Options.get()

     def Down():
       global vid
       video = ytThing.streams.get_by_resolution(vid)
       video.download()
       done = customtkinter.CTkLabel(screen,text="Done!")
       done.pack(pady= 10,padx=10)

     def AudioOnly():
       global vid
       video = ytThing.streams.get_audio_only()
       video.download()
       done = customtkinter.CTkLabel(screen,text="Done!")
       done.pack(pady= 10,padx=10)
                                 
        

     Dbutton = customtkinter.CTkButton(screen, text= "Download", command= Down)
     Dbutton.pack(pady= 60)

     Audio = customtkinter.CTkButton(screen,text= "Audio only",command= AudioOnly)
     Audio.pack(pady=10,padx=20)

     Options = customtkinter.CTkOptionMenu(screen, values= resolution, command= select)
     Options.pack(pady=40)
       
    else:
     screen = customtkinter.CTkToplevel(app)
     screen.title("Download")
     screen.geometry("500x300")

     NoLink = customtkinter.CTkLabel(screen,text= "ERROR please Enter a video link")
     NoLink.pack(pady= 40)

#link Input
urlVar = customtkinter.StringVar()
link = customtkinter.CTkEntry(app,placeholder_text= "Place link here",placeholder_text_color="blue",textvariable= urlVar,width= 300, height= 50)  
link.pack(pady= 40)

button = customtkinter.CTkButton(app,text= "submit",height= 50, width= 200,command= getV)
button.pack(pady= 60)





app.mainloop()