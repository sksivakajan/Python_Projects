import tkinter as tk
from tkinter import messagebox

# Function to evaluate expressions
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input!")
    return ""

# Function to update the input field
def click_button(item):
    current_text = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current_text + str(item))

# Function to clear the input field
def clear_input():
    input_field.delete(0, tk.END)

# Function to calculate the result
def calculate():
    expression = input_field.get()
    result = evaluate_expression(expression)
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, result)

# Initialize the main window
root = tk.Tk()
root.title("SK_Calculator")

# Input field
input_field = tk.Entry(root, width=35, borderwidth=10)
input_field.grid(row=0, column=0, columnspan=10, padx=20, pady=10)

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Loop to create buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: click_button(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text='C', padx=20, pady=20, command=clear_input).grid(row=5, column=0, columnspan=4)

# Run the application
root.mainloop()
