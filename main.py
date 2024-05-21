import tkinter 
from tkinter import ttk

archivo = open("C:/Users/pnico/Documents/Finall_proyect/finall_proyect/Datos_Vuelos _Finales.txt", "r")


window = tkinter.Tk()
window.title("Airline check-in system")
frame = tkinter.Frame(window)
frame.pack()

#getting de information of the user

get_data_of_fly = tkinter.LabelFrame(frame, text="Get data of fly")
get_data_of_fly.grid(row = 0, column = 2, padx = 20, pady = 20)

informatio1 = tkinter.Label(get_data_of_fly, text="Solo ida")
informatio1.grid (row = 0, column = 0) 

space = tkinter.Label(get_data_of_fly, text=" Holaaaa")
space.grid (row = 0, column = 1)
information2 = tkinter.Label (get_data_of_fly, text="Ocuppants")
information2.grid(row = 0, column = 2)

ocuppants_combobox = tkinter.Spinbox(get_data_of_fly, from_ = 1, to = 72)
ocuppants_combobox.grid(row = 1, column = 2)




window.mainloop()

