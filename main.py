import tkinter 
import customtkinter 
from PIL import ImageTk, Image

def first_window():
    #The apparence of the window set to the system mode
    customtkinter.set_appearance_mode ("system")
    customtkinter.set_default_color_theme ("green")

    app = customtkinter.CTk()
    app.title("My App")
    app.geometry("600x500")

    #The background image is set
    ########################################
    # image_background = ImageTk.PhotoImage(Image.open("background.jpg", "r"))
    # l1 = customtkinter.CTkLabel(master=app, image=image_background)
    # l1.pack()
    ########################################


    #now we gona do a frame 

    frame = customtkinter.CTkFrame(app)
    frame.place (relx = 0.5, rely = 0.5, anchor = "center")

    #now we goona do the options for the user

    option1 = customtkinter.CTkLabel(master=frame, text= "Welcome, pls select an option", font = ("Century Gothic", 15))
    option1.place ( x = 10, y = 45)
    app.mainloop()


if __name__ == "__main__":
    first_window()

