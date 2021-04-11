import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
	print("This is the entry:", entry)






root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Calculate Cost", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

fuel_button = tk.Button(frame, text ="Enter Fuel Type",font=40 , fg ="green")
#fuel_button.place(rely=2,relx=0.7, relheight=1, relwidth=0.3)

moto_button = tk.Button(frame, text ="Enter Moto Type", font=40 , fg ="red")
#moto_button.place(rely=3,relx=0.7, relheight=1, relwidth=0.3)

destination_button = tk.Button(frame, text ="Enter Destination",font=40 , fg ="green")
#destination_button.place(rely=4,relx=0.7, relheight=1, relwidth=0.3)

#lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
#lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

#label = tk.Label(lower_frame)
#label.place(relwidth=1, relheight=1)

root.mainloop()