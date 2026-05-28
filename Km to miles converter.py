#
# def add(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result
#
# operation = add(4, 6, 7, 8, 9)
# print(operation)
#
#
#








#
# import tkinter
#
# screen = tkinter.Tk()
# screen.title("My first Tkinter Application")
# screen.minsize(width=500, height= 300)
#
# my_text = tkinter.Label(text= "Dantex Eruzy", font=("Arial", 24))
# my_text.grid(column=0, row=0)
#
# def clicked():
#     my_text["text"] = entry.get().title()
#
# button = tkinter.Button(text= "Click", command= clicked)
# button.grid(column=1, row=1)
#
# entry = tkinter.Entry(width= 10)
# entry.grid(column=4, row=3)
#
# new_button = tkinter.Button(text= "New Button")
# new_button.grid(column=3, row=0)
#
# screen.mainloop()


import tkinter as t


window = t.Tk()
window.title(" Dantex Offical - Mile to Km Converter")
window.minsize(width=250, height=50)
window.config(padx=20, pady=10)

def maths():
    miles_value = miles_label_value.get()
    result = round(float(miles_value) * 1.60934, 1)
    KM_label_value["text"] = result



miles_label_value = t.Entry(width=10)
miles_label_value.grid(column=2, row=0)
miles_label_text = t.Label(text="Miles")
miles_label_text.grid(column=3, row=0)

is_equal = t.Label(text="is equal to")
is_equal.grid(column=0, row=1)

KM_label_value = t.Label(text= 0)
KM_label_value.config(pady=10)
KM_label_value.grid(column=2, row=1)

KM_label_text = t.Label(text= "Km")
KM_label_text.grid(column=3, row=1)

calculate_button = t.Button(text="Calculate",command=maths)
calculate_button.config(padx=20)
calculate_button.grid(row=2, column=2)








window.mainloop()

