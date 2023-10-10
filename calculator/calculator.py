import tkinter as tk

def button_click(value):
    current = result.get()
    result.delete(0, tk.END)
    result.insert(tk.END, current + value)

def calculate_result():
    try:
        expression = result.get()
        result.delete(0, tk.END)
        result.insert(tk.END, eval(expression))
    except:
        result.delete(0, tk.END)
        result.insert(tk.END, "Error")

def clear_result():
    result.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display
result = tk.Entry(window, width=30)
result.grid(row=0, column=0, columnspan=4)

# Create the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(window, text=button, command=calculate_result, width=5).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, command=lambda value=button: button_click(value), width=5).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(window, text="C", command=clear_result, width=5).grid(row=row, column=col)

# Start the main loop
window.mainloop()
