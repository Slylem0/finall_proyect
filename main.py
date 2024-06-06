import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import *
import tabulate
def get_data_flyes(origin, destine, users, date): 
            print (origin.cget("text") + "\n" + destine.cget("text") + "\n" + users.get() + "\n" + date.cget("text"))
            return (origin.cget("text") + "\n" + destine.cget("text") + "\n" + users.get() + "\n" + date.cget("text"))

def botton1_click():
    window3 = customtkinter.CTk()
    window3.title("Chek-in")
    window3.geometry("600x440")
    window3.resizable(False, False)

    frame = customtkinter.CTkFrame(master=window3, width=475, height=375, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    customtkinter.CTkLabel(master=frame, text="Check-in", font=("Century Gothic", 25)).place(x=180, y=10)

    customtkinter.CTkLabel(master=frame, text="Write the Number of your ticket", font=("Centuary Gothic", 15)).place(x=100, y=50)

    user_data = customtkinter.CTkEntry(master=frame, width=150, font=("Century Gothic", 15))
    user_data.place(x=180, y=100)


    botton_ckeck = customtkinter.CTkButton(master=frame, text="Check", corner_radius=10)
    botton_ckeck.place(x=180, y=150)
    window3.mainloop()

def button2_click():
    window2 = customtkinter.CTk()
    window2.title("Buy a ticket")
    window2.geometry("600x440")
    window2.resizable(False, False)

    frame = customtkinter.CTkFrame(master=window2, width=475, height=375, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    customtkinter.CTkLabel(master=frame, text="Origin", font=("Century Gothic", 15)).place(x=10, y=10)
    customtkinter.CTkLabel(master=frame, text="Origen", font=("Century Gothic", 15)).place(x=10, y=50)
    with open(fr"C:\Users\pnico\Downloads\Datos_Vuelos _Finales.txt", "r") as archivo:
        datos = archivo.readlines()

    lista_limpia = []
    for a in datos[1:]:
        a = a.split(",")
        lista_limpia.append(a)

    place_from = []
    for i in lista_limpia:
        # Remove spaces and quotes
        cleaned_data1 = i[7].replace(" ", "").replace("'", "")
        place_from.append(cleaned_data1)

    to_arrive = []
    for i in lista_limpia:
        # Remove spaces and quotes
        cleaned_data2 = i[8].replace(" ", "").replace("'", "").replace("]", "")
        to_arrive.append(cleaned_data2)

    date = []
    for i in lista_limpia:
        # Remove spaces and quotes
        cleaned_data3 = i[1].replace(" ", "").replace("'", "").replace("]", "")
        date.append(cleaned_data3)


    origin = place_from
    origin_variable = tkinter.StringVar(frame)
    origin_variable.set(place_from[0])
    drop = OptionMenu(frame, origin_variable, *origin)
    drop.place(x=10, y=70)


    destino = to_arrive

    destine_variable = tkinter.StringVar(frame)
    origin_variable.set(to_arrive[1])
    drop2 = OptionMenu(frame, destine_variable, *destino)
    drop2.place(x=10, y=150)

    date_variable = tkinter.StringVar(frame)
    date_variable.set(date[0])
    drop3 = OptionMenu(frame, date_variable, *date)
    drop3.place(x=10, y=220)


    age_label = tkinter.Label(master=frame, text="users", font=("Century Gothic", 15))
    age_spinbox = tkinter.Spinbox(master=frame, from_=1, to=72, font=("Century Gothic", 15))
    age_label.place(x=250, y=20)
    age_spinbox.place(x=250, y=80)



    botton = customtkinter.CTkButton(master=frame, text="Search", corner_radius=6, 
                                     command=lambda: get_data_flyes(drop, drop2, age_spinbox, drop3))
    botton.place(x=150, y=150)


    #now with the dates of the botton we goona do the table of the flights

    frame2 = customtkinter.CTkFrame(master=frame, width=450, height=200, corner_radius=15)
    frame2.place(x=10, y=200)
    customtkinter.CTkLabel(master=frame2, text="Flights", font=("Century Gothic", 15)).place(x=200, y=10)

    

    window2.mainloop()


def first_window():
    # The apparence of the window set to the system mode
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("green")

    app = customtkinter.CTk()
    app.title("My App")
    app.geometry("600x440")
    app.resizable(False, False)
    
    # The background image is set
    image_path = tkinter.PhotoImage(file=(fr"C:\Users\pnico\Downloads\Backgroung.png"))
    bg_image = tkinter.Label(app, image=image_path)
    bg_image.pack()


    # now we gona do a frame

    frame = customtkinter.CTkFrame(
                                    master = bg_image, width = 320, height = 360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # now we goona do the options for the user

    option1 = customtkinter.CTkLabel(master=frame,
                                     text="Welcome please select an option",
                                     font=("Century Gothic", 15))
    option1.place(x=10, y=45)
    image1 = PhotoImage(file=(fr"C:\Users\pnico\Documents\Finall_proyect\finall_proyect\images\Logo.png"))
    #ahora hacemos mas pequeña la imagen
    image1 = image1.subsample(6, 6)




    customtkinter.CTkLabel(frame, image = image1).place(x=120, y=70)

    ##now we goona do the buttons options for the user

    button1 = customtkinter.CTkButton(master=frame, width=220, text = "Chek-in", corner_radius = 6, command = botton1_click)
    button1.place(x=50, y=150)


    button2 = customtkinter.CTkButton(master=frame, width=220, text = "Buy a ticket", corner_radius=6, command=button2_click)
    button2.place(x=50, y=250)

    app.mainloop()
    app.geometry("600x500")

    # The background image is set
    ########################################
    image_path = tkinter.PhotoImage(file="./Backgroung.png")
    bg_image = tkinter.Label(app, image=image_path)
    bg_image.pack()
    ########################################
    # now we gona do a frame

    frame = customtkinter.CTkFrame(app)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # now we goona do the options for the user

    option1 = customtkinter.CTkLabel(master=frame,
                                     text="Welcome, pls select an option",
                                     font=("Century Gothic", 15))
    option1.place(x=10, y=45)

    app.mainloop()


if __name__ == "__main__":
    first_window()
