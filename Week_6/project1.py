import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    location = location_entry.get()
    weight = float(weight_entry.get())
    charge = 0
    
    if location.lower() == 'ibeju-lekki':
        charge = 5000 if weight >= 10 else 3500
    elif location.lower() == 'epe':
        charge = 10000 if weight >= 10 else 5000
    else:
        messagebox.showerror("Error", "Invalid location")
        return
    
    messagebox.showinfo("Delivery Charge", f"The delivery charge is: ₦{charge}")


root = tk.Tk()
root.title("Simi Services Delivery Charge Calculator")


tk.Label(root, text="Enter package location:").grid(row=0, column=0)
location_entry = tk.Entry(root)
location_entry.grid(row=0, column=1)

tk.Label(root, text="Enter package weight (kg):").grid(row=1, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_button.grid(row=2, column=0, columnspan=2)

root.mainloop()