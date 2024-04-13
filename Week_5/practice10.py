import tkinter as tk

#Handling button click event
def button_click():
    msgbox.showinfo("Info", "Welcome to COS 102 GUI app!\n")
    result = msgbox.askyesno("Confirmation", "Do you want to continue?")

root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

label = tk.Label(root,text="Hello Friend\n")
label.pack()

button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

button.config(fg="white", bg="black")

root.mainloop()