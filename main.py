from tkinter import *

def clear_text():
    user_input.delete(0, END)

def button_clicked():
    clear_text()
    result = 0
    result = int(user_input2.get())*1.609
    user_input.insert(END, result)
    print(result)
    return result


window = Tk()
window.title("Mile to Km Converter")



label = Label(text="Miles")
label.grid(column=2, row=1)

label2 = Label(text="Km")
label2.grid(column=2, row=2)


button = Button(text="calculate", command=button_clicked)
button.grid(column=1, row=3)

user_input = Entry()
user_input.grid(column=1, row=2)


user_input2 = Entry()
user_input2.grid(column=1, row=1)

window.mainloop()
