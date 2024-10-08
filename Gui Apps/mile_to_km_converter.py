from tkinter import *

def miles_to_kilometers():
    result = f"{float(input_miles.get()) * 1.60934:.1f}"
    result_label.config(text=str(result))

window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

# Miles label
label_miles = Label(window, text='Miles')
label_miles.grid(column=2, row=0)

# Is equal to label
label_is_equal_to = Label(window, text='is equal to')
label_is_equal_to.grid(column=0, row=1)

# Result label three
result_label = Label(window, text='0')
result_label.grid(column=1, row=1)

# Km label
km_label = Label(window, text='Km')
km_label.grid(column=2, row=1)

# Calculate Button
button_calculate = Button(window, text='Calculate', command=miles_to_kilometers)
button_calculate.grid(column=1, row=2)

# Entry
input_miles = Entry(window, width=5)
input_miles.grid(column=1, row=0)


window.mainloop()