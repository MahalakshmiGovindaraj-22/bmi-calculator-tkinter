import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("Input Error", "Enter positive numbers")
            return

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Healthy weight"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        elif bmi < 35:
            category = "Obesity"
            color = "purple"
        else:
            category = "Severe Obesity"
            color = "red"

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}", fg=color)

    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
