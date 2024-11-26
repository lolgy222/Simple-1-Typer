import tkinter as tk

def button_click(char):
    global expression
    expression += char
    equation.set(expression)

def equalto():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

expression = ""

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x150")

equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

button1 = tk.Button(root, text=' 1 ', fg='black', bg='gray',
                   command=lambda: button_click('1'), height=1, width=7)
button1.grid(row=2, column=0)

# Similarly, create buttons for other digits, operators, and functions

root.mainloop()