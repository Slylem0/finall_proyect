import tkinter 
import customtkinter 
from PIL import ImageTk, Image

def first_window():
    #The apparence of the window set to black
    customtkinter.set_appearance_mode ("system")
    customtkinter.set_default_color_theme ("green")

    app = customtkinter.CTk()
    app.title("My App")
    app.geometry("800x600")

    #The background image is set
    image_background = ImageTk.PhotoImage(Image.open("background.jpg", "r"))
    l1 = customtkinter.CTkLabel(master=app, image=image_background)
    l1.pack()

    app.mainloop()


if __name__ == "__main__":
    first_window()

