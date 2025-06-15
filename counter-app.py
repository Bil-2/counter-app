import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Counter App")
root.geometry("300x200")
root.resizable(False, False)

# Initialize counter variable
counter = tk.IntVar(value=0)

# Function to update label
def update_label():
    label.config(text=str(counter.get()))

# Button functions
def increment():
    counter.set(counter.get() + 1)
    update_label()

def decrement():
    counter.set(counter.get() - 1)
    update_label()

def reset():
    counter.set(0)
    update_label()

# UI elements
label = tk.Label(root, text="0", font=("Helvetica", 48), fg="black")
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

inc_btn = tk.Button(button_frame, text="+", font=("Helvetica", 20), width=5, command=increment)
inc_btn.grid(row=0, column=0, padx=5)

dec_btn = tk.Button(button_frame, text="-", font=("Helvetica", 20), width=5, command=decrement)
dec_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(root, text="Reset", font=("Helvetica", 14), width=10, command=reset)
reset_btn.pack(pady=10)

# Run the app
root.mainloop()
