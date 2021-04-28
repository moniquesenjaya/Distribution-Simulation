from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import tkinter as tk

def uniforming(a, b):
    height = 1 / (b - a)
    mean = (a + b) / 2
    sd = (b - a) / 12 ** (1/2)
    lin = np.linspace(0, (b + a), 100)
    return [a, b - a, height, mean, sd, lin]

root = Tk()
root.title("Distribution Simulation")
root.geometry("1280x720")

min_value = IntVar()
max_value = IntVar()
pdf_min_value = IntVar()
pdf_max_value = IntVar()

def graph_uniform():
    low = (min_value.get())
    high = (max_value.get())

    print(low, high)
    results = uniforming(low, high)

    y = uniform.pdf(results[-1], results[0], results[1])
    plt.plot(results[-1], y, "b-")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Uniform distribution for {low} -> {high}")
    # plt.grid(True)

    # For padding
    plt.tight_layout()

    # For filling in areas
    plt.fill_between(results[-1], y, alpha = 0.25)

    plt.show()

simulation_screen = ttk.Notebook(root)
simulation_screen.pack()

uniform_tab = Frame(simulation_screen, width=1280, height=720)
normal_tab = Frame(simulation_screen, width=1280, height=720)
uniform_tab.pack(fill="both", expand=1)
normal_tab.pack(fill="both", expand=1)

simulation_screen.add(uniform_tab, text="Uniform Distribution") 
simulation_screen.add(normal_tab, text="Normal Distribution")

title = Label(uniform_tab, text ='Uniform Distribution', font = ("sans-serif", 15, "bold")) 
title.place(x=550, y=5)

input_uniform_frame = Frame(uniform_tab, width=400, height=400, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_uniform_frame.place(x=20, y=50, width=400, height=300)

input_uniform_title = Label(input_uniform_frame, text="Input data", font=14)
input_uniform_title.grid(row=0, columnspan=2, pady=10, padx=10, sticky="w")

min_label = Label(input_uniform_frame, text = "Lower Bound (inclusive):", font=12)
min_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")
min_text = Entry(input_uniform_frame, font= 12, bd=2, relief=GROOVE, textvariable = min_value)
min_text.grid(row=1, column=1, padx=4, pady=5, sticky = "w", columnspan=2)

max_label = Label(input_uniform_frame, text = "Upper Bound (inclusive):", font=12)
max_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")
max_text = Entry(input_uniform_frame, font= 12, bd=2, relief=GROOVE, textvariable = max_value)
max_text.grid(row=2, column=1, padx=4, pady=20, sticky = "w", columnspan=2)

input_uniform_subtitle = Label(input_uniform_frame, text="Probability Distribution", font=14)
input_uniform_subtitle.grid(row=3, columnspan=2, padx=10, sticky="w")

input_uniformpdf_frame = Frame(input_uniform_frame, width=200, height=50)
input_uniformpdf_frame.grid(row=4, column=0, pady=10, padx=10, sticky="w")

pdf_min_text = Entry(input_uniformpdf_frame, font= 12, width=5, bd=2, relief=GROOVE, textvariable = pdf_min_value)
pdf_min_text.grid(row=0, column=0, padx=5, pady=5, sticky = "w")

pdf_text = Label(input_uniformpdf_frame, text=" < x < ", font=12)
pdf_text.grid(row=0, column=1, pady=5, sticky = "w")

pdf_max_text = Entry(input_uniformpdf_frame, font= 12, width=5, bd=2, relief=GROOVE, textvariable = pdf_max_value)
pdf_max_text.grid(row=0, column=2, pady=5, sticky = "w")

uniform_button = Button(input_uniformpdf_frame, text="Graph", bd=4, width =10, relief=GROOVE, command =lambda: graph_uniform())
uniform_button.grid(row=1, column=0, pady=25, columnspan=2)

title = Label(normal_tab, text ='Normal Distribution', font = ("sans-serif", 15, "bold")) 
title.place(x=550, y=5)

root.mainloop()
