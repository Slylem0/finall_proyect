# Import all libraries we gonna use
import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import PhotoImage, OptionMenu, Listbox, messagebox
from tkinter import *
import tabulate


# Starting making the functions that we will use
def get_data_flyes(origin, destine, users, date):
    print(origin.cget("text") + "\n" +
          destine.cget("text") + "\n" +
          users.get() + "\n" + date.cget("text"))

    return (origin.cget("text") + "\n" +
            destine.cget("text") + "\n" +
            users.get() + "\n" + date.cget("text"))


def botton1_click():
    window3 = customtkinter.CTk()
    window3.title("Chek-in")
    window3.geometry("600x440")
    window3.resizable(False, False)

    frame = customtkinter.CTkFrame(master=window3, width=475,
                                   height=375, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    customtkinter.CTkLabel(master=frame, text="Check-in",
                           font=("Century Gothic", 25)).place(x=180, y=10)

    customtkinter.CTkLabel(master=frame,
                           text="Write the Number of your ticket",
                           font=("Centuary Gothic", 15)).place(x=100, y=50)

    user_data = customtkinter.CTkEntry(master=frame,
                                       width=150,
                                       font=("Century Gothic", 15))
    user_data.place(x=180, y=100)

    botton_ckeck = customtkinter.CTkButton(master=frame,
                                           text="Check",
                                           corner_radius=10)
    botton_ckeck.place(x=180, y=150)
    window3.mainloop()


def button2_click():
    window2 = customtkinter.CTk()
    window2.title("Buy a ticket")
    window2.geometry("600x500")
    window2.resizable(False, False)

    frame = customtkinter.CTkFrame(master=window2, width=475,
                                   height=450, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    customtkinter.CTkLabel(master=frame, text="From",
                           font=("Century Gothic", 10)).place(x=10, y=10)
    customtkinter.CTkLabel(master=frame, text="To",
                           font=("Century Gothic", 10)).place(x=110, y=10)
    customtkinter.CTkLabel(master=frame, text="Travel dates",
                           font=("Century Gothic", 10)).place(x=215, y=10)

    with open("Datos_Vuelos_Finales.txt", "r") as archivo:
        datos = archivo.readlines()

    lista_limpia = []
    for a in datos[1:]:
        a = a.split(",")
        lista_limpia.append(a)

    place_from = []
    for i in lista_limpia:
        # Remove spaces and quotes
        cleaned_data1 = i[7].replace(" ", "").replace("'", "")
        if cleaned_data1 not in place_from:
            place_from.append(cleaned_data1)

    to_arrive = []
    for i in lista_limpia:
        # Remove spaces and quotes
        cleaned_data2 = (i[8].replace(" ", "").replace("'", "")
                         .replace("]", "").strip("\n"))
        if cleaned_data2 not in to_arrive:
            to_arrive.append(cleaned_data2)

    date = []
    for i in lista_limpia:
        # Remove spaces and quotes
        cleaned_data3 = i[1].replace(" ", "").replace("'", "").replace("]", "")
        if cleaned_data3 not in date:
            date.append(cleaned_data3)

    origin = place_from
    origin_variable = tkinter.StringVar(frame)
    origin_variable.set(place_from[0])
    drop = OptionMenu(frame, origin_variable, *origin)
    drop.place(x=10, y=50)
    drop.config(bg="gray")

    destino = to_arrive

    destine_variable = tkinter.StringVar(frame)
    destine_variable.set(to_arrive[2])
    drop2 = OptionMenu(frame, destine_variable, *destino)
    drop2.place(x=135, y=50)
    drop2.config(bg="gray")

    date_variable = tkinter.StringVar(frame)
    date_variable.set(date[0])
    drop3 = OptionMenu(frame, date_variable, *date)
    drop3.place(x=260, y=50)
    drop3.config(bg="gray")

    # now with the dates of the botton we goona do the table of the flights
    frame2 = customtkinter.CTkFrame(master=frame, width=450,
                                    height=110, corner_radius=15)
    frame2.place(x=10, y=120)
    customtkinter.CTkLabel(master=frame2, text="Sort by:",
                           font=("Century Gothic", 15)).place(x=10, y=10)

    lst_trips = Listbox(frame, width=68, height=3)
    lst_trips.place(x=20, y=200)

    def fill_lstbox():
        j = 0
        counter1 = 0
        counter2 = 0
        counter3 = 0
        ubi_flight_origin = []
        ubi_flight_destiny = []
        date_flight = []
        element_origin_place = (drop.cget("text"))
        element_destiny_place = drop2.cget("text")
        element_date = drop3.cget("text")
        lst_origin = []
        lst_destiny = []
        lst_dates = []

        for i in lista_limpia:
            cleaned_data4 = i[7].replace(" ", "").replace("'", "")
            lst_origin.append(cleaned_data4)

        for i in lista_limpia:
            cleaned_data5 = (i[8].replace(" ", "").replace("'", "")
                             .replace("]", "").strip("\n"))
            lst_destiny.append(cleaned_data5)

        for i in lista_limpia:
            cleaned_data6 = (i[1].replace(" ", "").replace("'", ""))
            lst_dates.append(cleaned_data6)

        for i in lst_destiny:
            if element_destiny_place == i:
                ubi_flight_destiny.append(counter2)
            counter2 += 1

        for i in lst_origin:
            if element_origin_place == i:
                ubi_flight_origin.append(counter1)
            counter1 += 1

        for i in lst_dates:
            if element_date == i:
                date_flight.append(counter3)
            counter3 += 1

        mix_lst = ubi_flight_origin + ubi_flight_destiny
        repeated = []
        for i in range(len(mix_lst)):
            for j in range(len(mix_lst)):
                if i != j:
                    if mix_lst[i] == mix_lst[j] and mix_lst[i] not in repeated:
                        repeated.append(mix_lst[i])

        global repeated_final

        second_mix_lst = repeated + date_flight
        repeated_final = []
        for i in range(len(second_mix_lst)):
            for j in range(len(second_mix_lst)):
                if i != j:
                    if (second_mix_lst[i] == second_mix_lst[j] and
                            second_mix_lst[i] not in repeated_final):
                        repeated_final.append(second_mix_lst[i])

        if repeated_final:
            lst_places_to_go = []
            lst_places_to_go.clear()
            for i in repeated_final:
                lst_places_to_go.append(lista_limpia[i][7] + " - " +
                                        lista_limpia[i][2] + "    -    " +
                                        lista_limpia[i][8] + " - " +
                                        lista_limpia[i][3].strip("\n") +
                                        ("  "*9) + "-From:    COP - " +
                                        lista_limpia[i][4])
            for i in lst_places_to_go:
                lst_trips.insert(j, i)
                j += 1
        else:
            message_empyty_lst = (("  "*16) + "There is not flight" +
                                  " for this date at the moment.")
            message_empyty2 = (("  "*20) +
                               "Please keep searching in other dates")
            lst_trips.insert(0, message_empyty_lst)
            lst_trips.insert(1, message_empyty2)

    def seat_info_more(kind):
        if kind == 1:
            messagebox.showinfo(title="Aluminium service", message=(
                """
    1 personal item (bag) (Must fit under the seat)
    1 hand luggage (10 kg) (From $195,100 COP)
    Hold luggage (23 kg) (From $175,600 COP)
    Economy Seat (Random-Rated Aluminum)
    Flight changes (Not allowed)
    Refund (Not allowed)"""))
        elif kind == 2:
            messagebox.showinfo(title="Diamond service", message=(
                """
    1 personal item (bag) (Must fit under the seat)
    1 checked baggage (23 kg) (Must fit in the overhead compartment)
    1 hand luggage (10 kg) (Deliver the luggage at the counter)
    Economy Seat (Specific rows available at random)
    Flight changes (Not allowed)
    Refund (Not allowed)"""))
        elif kind == 3:
            messagebox.showinfo(title="Diamond service", message=(
                """
    1 personal item (bag) (Must fit under the seat)
    1 hand luggage (10 kg) (Must fit in the overhead compartment)
    1 checked baggage (23 kg) (Deliver the baggage to the counter)
    Plus Seat (Subject to availability - Premium classification)
    Flight changes (No change fee, before the flight)
    Refund (Not allowed)"""))

    def buying_options():
        if repeated_final:
            for item in lst_trips.curselection():
                info = (lst_trips.get(item).replace(" ", "").replace("\n", "")
                        .split("-"))
            for i in repeated_final:
                if (lista_limpia[i][4] == info[5]):
                    ubi_data = i

            frame3 = customtkinter.CTkFrame(master=frame, width=120,
                                            height=160, corner_radius=15)
            frame3.place(x=30, y=270)
            customtkinter.CTkLabel(
                master=frame3, text="Aluminium",
                font=("Century Gothic", 12)).place(x=10, y=5)
            customtkinter.CTkLabel(master=frame3, text="COP " + info[5],
                                   font=(
                                       "Century Gothic", 12)).place(x=10, y=30)
            botton_more_info = customtkinter.CTkButton(
                master=frame3, text="More information", corner_radius=6,
                width=100, font=("Century Gothic", 10), command=lambda:
                [seat_info_more(1)])
            botton_more_info.place(x=10, y=80)
            botton_aluminium = customtkinter.CTkButton(
                master=frame3, text="Select", corner_radius=6,
                width=100, command=lambda: [])
            botton_aluminium.place(x=10, y=120)

            frame4 = customtkinter.CTkFrame(master=frame, width=120,
                                            height=160, corner_radius=15)
            frame4.place(x=180, y=270)
            customtkinter.CTkLabel(
                master=frame4, text="Diamond",
                font=("Century Gothic", 12)).place(x=10, y=5)
            customtkinter.CTkLabel(
                master=frame4, text="COP " + lista_limpia[ubi_data][5],
                font=("Century Gothic", 12)).place(x=10, y=30)
            botton_more_info_diamond = customtkinter.CTkButton(
                master=frame4, text="More information", corner_radius=6,
                width=100, font=("Century Gothic", 10), command=lambda:
                [seat_info_more(2)])
            botton_more_info_diamond.place(x=10, y=80)
            botton_diamond = customtkinter.CTkButton(
                master=frame4, text="Select", corner_radius=6,
                width=100, command=lambda: [])
            botton_diamond.place(x=10, y=120)

            frame5 = customtkinter.CTkFrame(master=frame, width=120,
                                            height=160, corner_radius=15)
            frame5.place(x=320, y=270)
            customtkinter.CTkLabel(
                master=frame5, text="Premium",
                font=("Century Gothic", 12)).place(x=10, y=5)
            customtkinter.CTkLabel(
                master=frame5, text="COP " + lista_limpia[ubi_data][6],
                font=("Century Gothic", 12)).place(x=10, y=30)
            botton_more_info_premium = customtkinter.CTkButton(
                master=frame5, text="More information",
                corner_radius=6, width=100,
                font=("Century Gothic", 10), command=lambda:
                [seat_info_more(3)])
            botton_more_info_premium.place(x=10, y=80)
            botton_premium = customtkinter.CTkButton(
                master=frame5, text="Select", corner_radius=6,
                width=100, command=lambda: [])
            botton_premium.place(x=10, y=120)
        else:
            messagebox.showwarning(title="Error no dates taken", message="""
    You may took a wrong selection
    Please select a correct travel date""")

    botton = customtkinter.CTkButton(master=frame,
                                     text="Search",
                                     corner_radius=6,
                                     command=lambda: [lst_trips.delete(0, END),
                                                      fill_lstbox()])
    botton.place(x=170, y=80)

    botton2 = customtkinter.CTkButton(master=frame,
                                      text="Buy",
                                      corner_radius=6,
                                      command=lambda: [buying_options()])
    botton2.place(x=170, y=235)

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
    image_path = tkinter.PhotoImage(file=("./images/Backgroung.png"))
    bg_image = tkinter.Label(app, image=image_path)
    bg_image.pack()

    # now we gona do a frame
    frame = customtkinter.CTkFrame(
                                    master=bg_image, width=320,
                                    height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # now we goona do the options for the user
    option1 = customtkinter.CTkLabel(master=frame,
                                     text="Welcome please select an option",
                                     font=("Century Gothic", 15))
    option1.place(x=10, y=45)
    image1 = PhotoImage(file=("./images/Logo.png"))
    # ahora hacemos mas pequeña la imagen
    image1 = image1.subsample(6, 6)

    customtkinter.CTkLabel(frame, image=image1).place(x=120, y=70)

    # now we goona do the buttons options for the user
    button1 = customtkinter.CTkButton(master=frame,
                                      width=220,
                                      text="Chek-in",
                                      corner_radius=6,
                                      command=botton1_click)
    button1.place(x=50, y=150)

    button2 = customtkinter.CTkButton(master=frame,
                                      width=220,
                                      text="Buy a ticket",
                                      corner_radius=6,
                                      command=button2_click)
    button2.place(x=50, y=250)

    app.mainloop()
    app.geometry("600x500")

    # The background image is set
    ########################################
    image_path = tkinter.PhotoImage(file="./images/Backgroung.png")
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
