from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import graph

# * Window initialization
root = Tk()
root.title("Distribution Simulation")
root.geometry("1280x720")
root.resizable(0, 0)    # Make root window fixed size

simulation_screen = ttk.Notebook(root)
simulation_screen.pack()

uniform_tab = Frame(simulation_screen, width = 1280, height = 720)
normal_tab = Frame(simulation_screen, width = 1280, height = 720)
uniform_tab.pack(fill = "both", expand = 1)
normal_tab.pack(fill = "both", expand = 1)

simulation_screen.add(uniform_tab, text = "Uniform Distribution")
simulation_screen.add(normal_tab, text = "Normal Distribution")

# * --------------------------------------------------------------- * #

# * Uniform Distribution graph initialization
titleUniform = Label(uniform_tab, text ='Uniform Distribution', font = ("sans-serif", 15, "bold"))
titleUniform.place(x = 550, y = 5)

graph_frame = Frame(uniform_tab, width = 1280, height = 500, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
graph_frame.place(x = 0, y = 0, width = 1280, height = 500)

figureUniform = plt.Figure(figsize = (5,4), dpi = 100)
a = figureUniform.add_subplot(1, 1, 1)
lowUniform = 5
highUniform = 10

results = graph.uniforming(lowUniform, highUniform)

y = uniform.pdf(results[-1], results[0], results[1])
a.plot(results[-1], y, "b-")

a.set_xlabel("x")
a.set_ylabel("y")
a.set_title("Uniform distribution")

# For padding
figureUniform.tight_layout()

# For filling in areas
a.fill_between(results[-1], y, alpha = 0.25)

canvas = FigureCanvasTkAgg(figureUniform, graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
# toolbar = NavigationToolbar2Tk(canvas, uniform_tab)
# toolbar.update()
canvas._tkcanvas.pack(side = TOP, fill = BOTH, expand = True)

# * --------------------------------------------------------------- * #

# * Uniform Distribution tab handling
def updateUniform():
    # Clear the subplot
    global a
    a.clear()

    # Get new lower and upper boundary from sliders
    low = slider1Uniform.get()
    high = slider2Uniform.get()

    # Plot new data into subplot
    results = graph.uniforming(low, high)

    y = uniform.pdf(results[-1], results[0], results[1])

    a.plot(results[-1], y, "b-")

    a.set_xlabel("x")
    a.set_ylabel("y")
    a.set_title("Uniform distribution")

    # For padding
    figureUniform.tight_layout()

    # For filling in areas
    a.fill_between(results[-1], y, alpha = 0.25)

    # Refresh canvas
    canvas.draw()

ui_frame = Frame(uniform_tab, width = 1280, height = 220, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
ui_frame.place(x = 0, y = 500, width = 1280, height = 220)

slider1Uniform = Scale(ui_frame, from_ = 1.0, to = 15, orient = HORIZONTAL, resolution = 0.1, length = 300)
slider1Uniform.set(5.0)
slider1Uniform.pack()

slider2Uniform = Scale(ui_frame, from_ = 1.0, to = 15, orient = HORIZONTAL, resolution = 0.1, length = 300)
slider2Uniform.set(10.0)
slider2Uniform.pack()

uniformButton = Button(ui_frame, text = "Update", bd = 4, width = 10, relief = GROOVE, command = lambda: updateUniform())
uniformButton.pack()

# * --------------------------------------------------------------- * #

# * Normal Distribution initialization
titleNormal = Label(normal_tab, text ='Normal Distribution', font = ("sans-serif", 15, "bold"))
titleNormal.place(x = 550, y = 5)

frameNormal = Frame(normal_tab, width = 1280, height = 500, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
frameNormal.place(x = 0, y = 0, width = 1280, height = 500)

figureNormal = plt.Figure(figsize = (5,4), dpi = 100)
b = figureNormal.add_subplot(1, 1, 1)
meanNormal = 0
stdNormal = 1

resultNormal = graph.normaling(meanNormal, stdNormal)

b.hist(resultNormal[1], density = 1)
b.plot(np.sort(resultNormal[1]), resultNormal[2])

b.set_xlabel("x")
b.set_ylabel("y")
b.set_title("Normal distribution")

# For padding
figureNormal.tight_layout()

canvasNormal = FigureCanvasTkAgg(figureNormal, frameNormal)
canvasNormal.draw()
canvasNormal.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
# toolbarNormal = NavigationToolbar2Tk(canvasNormal, normal_tab)
# toolbarNormal.update()
canvasNormal._tkcanvas.pack(side = TOP, fill = BOTH, expand = True)

uiFrameNormal = Frame(normal_tab, width = 1280, height = 220, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
uiFrameNormal.place(x = 0, y = 500, width = 1280, height = 220)

# * --------------------------------------------------------------- * #

# * Normal Distribution tab handling

# * Main loop
if __name__ == "__main__":
    root.mainloop()
