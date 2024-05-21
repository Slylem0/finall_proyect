import tkinter 
from tkinter import ttk

archivo = open("C:/Users/pnico/Documents/Finall_proyect/finall_proyect/Datos_Vuelos _Finales.txt", "r")


window = tkinter.Tk()
window.title("Airline check-in system")
frame = tkinter.Frame(window)
frame.pack()

#getting de information of the user

get_data_of_fly = tkinter.LabelFrame(frame, text="Get data of fly")
get_data_of_fly.grid(row = 0, column = 0, padx = 20, pady = 20)

informatio1 = tkinter.Label(get_data_of_fly, text="Solo ida")
informatio1.grid (row = 0, column = 0) 

information2 = tkinter.Label (get_data_of_fly, text="Ocuppants")
information2.grid(row = 0, column = 2)

ocuppants_combobox = ttk.Combobox(get_data_of_fly, values = [1,2,3,4,5,6,7,8,9,10, "More?, Write it: "])
ocuppants_combobox.grid(row = 1, column = 2)




window.mainloop()

