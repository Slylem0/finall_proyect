import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import *
from tkinter import OptionMenu, messagebox, Listbox, PhotoImage, StringVar, END
import tkinter.messagebox as messagebox
import random


def ticketfinal():
    global first
    global names
    first = ""

    with open("Codigos_Vuelos.txt", "a") as archivo:

        window9 = customtkinter.CTk()
        window9.title("Ticket")
        window9.geometry("250x100")
        window9.resizable(False, False)
        alfabhet = ["A", "B", "C", "D", "E", "F",
                    "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R",
                    "S", "T", "U", "V", "W", "X", "Y", "Z"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        for i in alfabhet:
            if i == names[0][0]:
                first += i
        first += "-"

        frame = customtkinter.CTkFrame(master=window9, width=230,
                                       height=80, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        for i in range(1, 4):
            first += random.choice(alfabhet)
            first += random.choice(numbers)

        archivo.write(first)
        archivo.write("\n")

        archivo.close()

        customtkinter.CTkLabel(master=frame, text="Ticket", font=(
            "Century Gothic", 18)).place(x=10, y=5)
        customtkinter.CTkLabel(master=frame, text=f"{first}", font=(
            "Century Gothic", 15)).place(x=10, y=35)

        window9.mainloop()


def comprobate_payment(card_number, cvv, window6):

    card_number = card_number.get()
    cvv = cvv.get()

    # Directly check the length of the card number
    if len(card_number) == 16:
        # Directly check the length of the CVV
        if len(cvv) == 3:
            messagebox.showinfo(
                title="Payment", message="The payment was successful")
            ticketfinal()
        else:
            messagebox.showerror(
                title="CVV Error", message="The CVV is incorrect")
    else:
        messagebox.showerror(
            title="Card Number Error", message="The card number is incorrect")

    window6.mainloop()


def card_payment():
    global ubi_data
    try:
        window6 = customtkinter.CTk()
        window6.title("Payment")
        window6.geometry("600x440")
        window6.resizable(False, False)

        def price_for_the_flight():
            if kinda == "Aluminium":
                return lista_limpia[ubi_data][4]
            if kinda == "Diamond":
                return lista_limpia[ubi_data][5]
            if kinda == "Premium":
                return lista_limpia[ubi_data][6]

        frame = customtkinter.CTkFrame(master=window6, width=500,
                                       height=450, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        customtkinter.CTkLabel(
            master=frame, text="Card Number",
            font=("Century Gothic", 15)).place(x=10, y=10)
        card_number = customtkinter.CTkEntry(
            master=frame, width=190,
            font=("Century Gothic", 15), corner_radius=40)
        card_number.place(x=10, y=50)

        customtkinter.CTkLabel(
            master=frame, text="Expiration Date",
            font=("Century Gothic", 15)).place(x=300, y=10)
        months = ["January", "February", "March", "April",
                  "May", "June", "July", "August",
                  "September", "October", "November", "December"]
        months_variable = StringVar(frame)
        months_variable.set(months[0])
        drop = OptionMenu(frame, months_variable, *months)
        drop.place(x=400, y=50)

        years = [i for i in range(2025, 2040)]
        years_variable = StringVar(frame)
        years_variable.set(years[0])
        drop2 = OptionMenu(frame, years_variable, *years)
        drop2.place(x=500, y=50)

        customtkinter.CTkLabel(
            master=frame, text="CVV",
            font=("Century Gothic", 15)).place(x=10, y=100)
        cvv = customtkinter.CTkEntry(master=frame, width=150,
                                     font=("Century Gothic", 15))
        cvv.place(x=10, y=150)

        customtkinter.CTkButton(
            master=frame, text="Pay", corner_radius=6,
            command=lambda: comprobate_payment(
                card_number, cvv, window6)).place(x=10, y=250)

        customtkinter.CTkLabel(
            master=frame, text="Total to pay:\nCOP $" +
            price_for_the_flight(),
            font=("Century Gothic", 15), bg_color="gray",
            text_color="black", corner_radius=10).place(x=300, y=245)

        window6.mainloop()
    except Exception as e:
        print(f"Error: {e}")


def comprobate_user(first_name, last_name, email, phone, window5):
    global names

    correo = email.get()
    phone = phone.get()
    first_name = first_name.get()
    last_name = last_name.get()

    names = [first_name, last_name]

    phone_contador = 0
    contador = 0
    try:
        for i in correo:
            if i == "@":
                contador += 1
            elif contador == 1 and i == ".":
                contador += 1
            elif contador >= 2 and i == ".":
                contador += 1
        if contador == 2:
            if isinstance(int(phone), int):
                phone_contador += 1
            if len(phone) == 10 and phone_contador == 1:
                card_payment()
        elif contador < 2 or contador > 2:
            messagebox.showerror(
                title="Email Error",
                message=("Your email is not valid" +
                         "\nWrite just one @ for the email" +
                         "\nWrite just one dot after @"))
    except Exception:
        messagebox.showerror(title="Phone Number Error",
                             message="Phone number is incorrect")

    window5.mainloop()


def _get_data():
    window5 = customtkinter.CTk()
    window5.title("Data")
    window5.geometry("600x440")
    window5.resizable(False, False)

    frame = customtkinter.CTkFrame(
        master=window5, width=500, height=450, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    customtkinter.CTkLabel(
        master=frame, text="First Name",
        font=("Century Gothic", 15)).place(x=10, y=10)
    first_name = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    first_name.place(x=10, y=50)

    customtkinter.CTkLabel(
        master=frame, text="Last Name",
        font=("Century Gothic", 15)).place(x=400, y=10)
    last_name = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    last_name.place(x=350, y=50)

    customtkinter.CTkLabel(
        master=frame, text="Gender",
        font=("Century Gothic", 15)).place(x=10, y=100)
    gender = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    gender.place(x=10, y=150)

    customtkinter.CTkLabel(
        master=frame, text="Nacionality",
        font=("Century Gothic", 15)).place(x=400, y=100)
    nacionality = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    nacionality.place(x=350, y=150)

    customtkinter.CTkLabel(
        master=frame, text="Number ID",
        font=("Century Gothic", 15)).place(x=10, y=200)
    number_id = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    number_id.place(x=10, y=250)

    customtkinter.CTkLabel(
        master=frame, text="Born Date",
        font=("Century Gothic", 15)).place(x=400, y=200)
    born_date = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    born_date.place(x=350, y=250)

    customtkinter.CTkLabel(
        master=frame, text="Asistence fly",
        font=("Century Gothic", 15)).place(x=10, y=300)
    asistence_fly = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    asistence_fly.place(x=10, y=330)

    customtkinter.CTkLabel(
        master=frame, text="Email",
        font=("Century Gothic", 15)).place(x=400, y=300)
    email = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    email.place(x=350, y=350)

    customtkinter.CTkLabel(
        master=frame, text="Phone",
        font=("Century Gothic", 15)).place(x=10, y=380)
    phone = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 15))
    phone.place(x=10, y=410)

    customtkinter.CTkButton(
        master=frame, text="Buy",
        corner_radius=6, command=lambda: comprobate_user(
            first_name, last_name, email, phone, window5)).place(x=350, y=410)

    window5.mainloop()


def buy_ticket(category):
    global final_seat
    global kinda
    kinda = category
    category = category

    window4 = customtkinter.CTk()
    window4.title("Seats")
    window4.geometry("600x440")
    window4.resizable(False, False)

    # Marco para los asientos
    frame_asientos = customtkinter.CTkFrame(
        master=window4, width=475, height=375, corner_radius=15)
    frame_asientos.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Agregar letras en la parte superior de las columnas
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    for j in range(6):
        customtkinter.CTkLabel(
            master=frame_asientos, text=letras[j]).grid(row=0, column=j+1)

    matrix_asientos = [[0 for i in range(6)] for j in range(12)]

    # Comenzar en 1 para ajustar por las etiquetas de letras
    for i in range(1, 13):
        # Enumerar las filas
        customtkinter.CTkLabel(
            master=frame_asientos, text=str(i)).grid(row=i, column=0)
        for j in range(6):
            matrix_asientos[i-1][j] = customtkinter.CTkButton(
                master=frame_asientos, text="Asiento",
                corner_radius=1, width=20, height=20)
            matrix_asientos[i-1][j].grid(row=i, column=j+1)
            # Ajustar índices para las etiquetas

    customtkinter.CTkLabel(
        master=window4, text="Seat",
        font=("Century Gothic", 15), bg_color="white",
        text_color="black", corner_radius=10).place(x=10, y=100)

    customtkinter.CTkButton(
        master=window4, text="Select",
        corner_radius=6, command=_get_data,
        width=120).place(x=5, y=300)

    if category == "Aluminium":
        customtkinter.CTkLabel(
            master=window4, text="Your Seat is Aleatory",
            font=("Century Gothic", 13)).place(x=10, y=150)
        column = ["A", "B", "C", "D", "E", "F"]
        b = column[random.randint(0, 5)]
        a = random.randint(1, 12)
        seat = f"{b} - {a}"
        final_seat = customtkinter.CTkLabel(
            master=window4, text=f"{seat}",
            font=("Century Gothic", 12)).place(x=15, y=200)

    elif category == "Diamond":
        customtkinter.CTkLabel(
            master=window4, text="Your file is aleatory",
            font=("Century Gothic", 13)).place(x=10, y=150)
        column = ["A", "B", "C", "D", "E", "F"]
        a = random.randint(1, 12)
        final_seat = customtkinter.CTkLabel(
            master=window4, text=f"Your file is {random.randint(1, 12)}",
            font=("Century Gothic", 12)).place(x=5, y=200)

        customtkinter.CTkEntry(
            master=window4, width=80,
            font=("Century Gothic", 15)).place(x=10, y=250)

    elif category == "Premium":
        customtkinter.CTkLabel(
            master=window4, text="You can select the seat",
            font=("Century Gothic", 10)).place(x=5, y=150)
        final_seat = customtkinter.CTkEntry(
            master=window4, width=80,
            font=("Century Gothic", 15)).place(x=10, y=200)

    customtkinter.CTkButton(
        master=window4, text="Buy",
        corner_radius=6, command=_get_data,
        width=120).place(x=5, y=300)

    window4.mainloop()


def comprube_data(code):
    with open("Codigos_Vuelos.txt", "r") as archivo:
        tckets = []
        counter = 0
        no_checkin_in_twice = []
        for line in archivo:
            tckets.append(line.strip())
        for i in range(len(tckets)):
            counter += 1
            if tckets[i] == code:
                messagebox.showinfo(
                    title="Check-in",
                    message="The code is correct."
                    "\nYou have done the Check-in")
                counter -= 1
                no_checkin_in_twice.append(code)
            elif counter == len(tckets):
                messagebox.showerror(
                    title="Chek-in Error",
                    message="The code is incorrect",)


def button1_click():

    window3 = customtkinter.CTk()
    window3.title("Chek-in")
    window3.geometry("600x500")
    window3.resizable(False, False)

    frame = customtkinter.CTkFrame(
        master=window3, width=475, height=450, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    customtkinter.CTkLabel(
        master=frame, text="Number of Code",
        font=("Century Gothic", 20)).place(x=150, y=150)
    code = customtkinter.CTkEntry(
        master=frame, width=150, font=("Century Gothic", 10))
    code.place(x=150, y=220)

    button4 = customtkinter.CTkButton(
        master=frame, text="Check",
        corner_radius=6, command=lambda: [comprube_data(code.get())])
    button4.place(x=150, y=300)

    window3.mainloop()


def botton2_click():
    window2 = customtkinter.CTk()
    window2.title("Buy a ticket")
    window2.geometry("600x500")
    window2.resizable(False, False)
    global lista_limpia

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
        global ubi_data
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
                width=100, command=lambda: [buy_ticket("Aluminium")])
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
                width=100, command=lambda: [buy_ticket("Diamond")])
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
                width=100, command=lambda: [(buy_ticket("Premium"))])
            botton_premium.place(x=10, y=120)
        else:
            messagebox.showwarning(title="Error no dates taken",
                                   message="""
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
        master=bg_image, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # now we goona do the options for the user

    option1 = customtkinter.CTkLabel(master=frame,
                                     text="Welcome please select an option",
                                     font=("Century Gothic", 15),
                                     bg_color="lightgray", fg_color="gray",
                                     text_color="black")
    option1.place(x=40, y=45)
    image1 = PhotoImage(file=("./images/Logo.png"))
    # ahora hacemos mas pequeña la imagen
    image1 = image1.subsample(6, 6)

    customtkinter.CTkLabel(frame, image=image1, text="").place(x=120, y=100)

    # now we goona do the buttons options for the user

    button1 = customtkinter.CTkButton(master=frame, width=220,
                                      text="Chek-in",
                                      corner_radius=6, command=button1_click)
    button1.place(x=50, y=200)

    button2 = customtkinter.CTkButton(master=frame, width=220,
                                      text="Buy a ticket",
                                      corner_radius=6, command=botton2_click)
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
                                     text="Welcome, please select an option",
                                     font=("Century Gothic", 15))
    option1.place(x=40, y=45)

    app.mainloop()


if __name__ == "__main__":
    first_window()
