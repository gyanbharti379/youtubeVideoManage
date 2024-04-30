import tkinter as tk

def show_choice():
    print("Selected option:", choice.get())

# Create the main window
root = tk.Tk()
root.title("Radio Button Group Example")

# Create a variable to hold the selected choice
choice = tk.StringVar()

# Create radio button group 1
group1_label = tk.Label(root, text="Group 1:")
group1_label.pack()
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=choice, value="Option 1", command=show_choice)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=choice, value="Option 2", command=show_choice)
radio_button3 = tk.Radiobutton(root, text="Option 3", variable=choice, value="Option 3", command=show_choice)
radio_button1.pack(anchor=tk.W)
radio_button2.pack(anchor=tk.W)
radio_button3.pack(anchor=tk.W)

# Create radio button group 2
group2_label = tk.Label(root, text="Group 2:")
group2_label.pack()
radio_button4 = tk.Radiobutton(root, text="Option A", variable=choice, value="Option A", command=show_choice)
radio_button5 = tk.Radiobutton(root, text="Option B", variable=choice, value="Option B", command=show_choice)
radio_button6 = tk.Radiobutton(root, text="Option C", variable=choice, value="Option C", command=show_choice)
radio_button4.pack(anchor=tk.W)
radio_button5.pack(anchor=tk.W)
radio_button6.pack(anchor=tk.W)

# Run the main event loop
root.mainloop()