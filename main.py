from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
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

def update():
    low = slider1.get()
    high = slider2.get()

    results = uniforming(low, high)

    y = uniform.pdf(results[-1], results[0], results[1])
    a.plot(results[-1], y, "b-")

    a.set_xlabel("x")
    a.set_ylabel("y")
    a.set_title(f"Uniform distribution")
    # plt.grid(True)

    # For padding
    figure2.tight_layout()

    # For filling in areas
    a.fill_between(results[-1], y, alpha = 0.25)

    canvas = FigureCanvasTkAgg(figure2, graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

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

graph_frame = Frame(uniform_tab, width=1280, height=500, highlightbackground="black", highlightcolor="black", highlightthickness=1)
graph_frame.place(x=0, y=0, width=1280, height=500)

figure2 = plt.Figure(figsize=(5,4), dpi=100)
a = figure2.add_subplot(111)
low = 5
high = 10

results = uniforming(low, high)

y = uniform.pdf(results[-1], results[0], results[1])
a.plot(results[-1], y, "b-")

a.set_xlabel("x")
a.set_ylabel("y")
a.set_title(f"Uniform distribution")
# plt.grid(True)

# For padding
figure2.tight_layout()

# For filling in areas
a.fill_between(results[-1], y, alpha = 0.25)

canvas = FigureCanvasTkAgg(figure2, graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
toolbar = NavigationToolbar2Tk(canvas, uniform_tab)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)


ui_frame = Frame(uniform_tab, width=1280, height=220, highlightbackground="black", highlightcolor="black", highlightthickness=1)
ui_frame.place(x=0, y=500, width=1280, height=220)

slider1 = Scale(ui_frame, from_= 0, to=15, orient=HORIZONTAL, resolution=0.1, length=300)
slider1.set(5.0)
slider1.pack()

slider2 = Scale(ui_frame, from_= 0, to=15, orient=HORIZONTAL, resolution=0.1, length=300)
slider2.set(10.0)
slider2.pack()

uniform_button = Button(ui_frame, text="Update", bd=4, width =10, relief=GROOVE, command =lambda: update())
uniform_button.pack()

title = Label(normal_tab, text ='Normal Distribution', font = ("sans-serif", 15, "bold")) 
title.place(x=550, y=5)

root.mainloop()
