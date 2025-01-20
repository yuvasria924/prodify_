# Import necessary libraries
from tkinter import *
from tkinter import ttk

# Functions
def celsius_to_fahrenheit(celsius):
    fahrenheit = 32 + celsius * 1.8
    return round(fahrenheit, 3)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return round(celsius, 3)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273
    return round(celsius, 3)

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return round(kelvin, 3)

# Conversion logic
def convert():
    try:
        celsius = Celsius_input.get(1.0, END).strip()
        fahrenheit = Fahrenheit_input.get(1.0, END).strip()
        kelvin = Kelvin_input.get(1.0, END).strip()

        if len(celsius) > 0:
            celsius = float(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
        elif len(fahrenheit) > 0:
            fahrenheit = float(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = celsius_to_kelvin(celsius)
        elif len(kelvin) > 0:
            kelvin = float(kelvin)
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = celsius_to_fahrenheit(celsius)

        Celsius_input.delete(1.0, END)
        Celsius_input.insert(END, celsius)
        Fahrenheit_input.delete(1.0, END)
        Fahrenheit_input.insert(END, fahrenheit)
        Kelvin_input.delete(1.0, END)
        Kelvin_input.insert(END, kelvin)

    except ValueError:
        print("Error: Invalid input")

# Clear input fields
def clear():
    Celsius_input.delete(1.0, END)
    Fahrenheit_input.delete(1.0, END)
    Kelvin_input.delete(1.0, END)

# GUI Window
root = Tk()
root.geometry("500x400")
root.resizable(0, 0)
root.config(bg="ghost white")
root.title("Convert Temperature")

# GUI Labels
Label(root, text="Celsius", font="arial 20 bold").place(x=50, y=50)
Label(root, text="Fahrenheit", font="arial 20 bold").place(x=50, y=125)
Label(root, text="Kelvin", font="arial 20 bold").place(x=50, y=200)

# Input Fields
Celsius_input = Text(root, font="arial 20", height=1, wrap=WORD, padx=5, pady=5)
Celsius_input.place(x=225, y=50)

Fahrenheit_input = Text(root, font="arial 20", height=1, wrap=WORD, padx=5, pady=5)
Fahrenheit_input.place(x=225, y=125)

Kelvin_input = Text(root, font="arial 20", height=1, wrap=WORD, padx=5, pady=5)
Kelvin_input.place(x=225, y=200)

# Buttons
Button(root, text="Convert", font="arial 20 bold", command=convert, bg="light green").place(x=100, y=300)
Button(root, text="Clear", font="arial 20 bold", command=clear, bg="red").place(x=300, y=300)

# Run the application
root.mainloop()
