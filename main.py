from tkinter import *

window = Tk()
window.title('Miles to Km Converter ')
window.minsize(width = 500, height = 300)
window.config(padx = 50, pady = 50)

def converter():
    """This is the function to convert the miles to kilometeres"""
    txt = float(input.get())
    conversion = txt *  1.60934
    rounded = round(conversion, 2)
    answer_label.config(text=rounded)
    print(rounded)




# Labels

# Answer
answer_label = Label(text='0',font = ('Times New Roman', 15, 'italic') )
answer_label.grid(column = 1, row = 1)

# Miles
mile_label = Label(text= 'Miles',font = ('Times New Roman', 15) )
mile_label.grid(column = 2, row = 0)

# KM
km_label = Label(text= 'KM',font = ('Times New Roman', 15) )
km_label.grid(column = 2, row = 1)

# Equals
equals = Label(text= 'is equal to',font = ('Times New Roman', 15) )
equals.grid(column = 0, row = 1)


# Entry
input = Entry(width = 10)
input.insert(0, '0')
input.grid(column = 1, row = 0, padx = 10, pady =10, ipady = 10)

# Command - Calculate
calculate = Button(text = 'Calculate', command= converter)
calculate.grid(column = 1, row = 2)






window.mainloop()