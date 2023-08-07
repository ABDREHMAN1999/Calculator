import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Fixed Size Calculator")
root.geometry("300x400")  # Fixed size

# Entry widget for display
entry = tk.Entry(root, font=("Arial", 16), borderwidth=5, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Button style
button_style = {
    "font": ("Arial", 14),
    "width": 5,
    "height": 2,
    "bg": "yellow"
}

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, **button_style, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='C', **button_style, command=button_clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

# Equal button
equal_button = tk.Button(root, text='=', **button_style, command=button_equal)
equal_button.grid(row=5, column=1, padx=5, pady=5, columnspan=2)

# Disable resizing of the window
root.resizable(width=False, height=False)

root.mainloop()
