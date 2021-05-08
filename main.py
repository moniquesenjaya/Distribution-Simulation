from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import graph
from tkinter import messagebox

# * Window initialization
root = Tk()
root.title("Distribution Simulation")
root.geometry("1280x720")
root.resizable(0, 0)    # Make root window fixed size

simulation_screen = ttk.Notebook(root)
simulation_screen.pack()

mean = StringVar()
sd = StringVar()
areaUpdate = StringVar()

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

mean.set(str(results[3]))
sd.set(str(results[4]))
areaUpdate.set(results[2] * results[1])

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
    # Get new lower and upper boundary from sliders
    low = slider1Uniform.get()
    high = slider2Uniform.get()

    if low > high:
        messagebox.showerror("Value Error", "Value of a should be more than b.")
        return

    # Clear the subplot
    global a
    a.clear()

    # Plot new data into subplot
    results = graph.uniforming(low, high)

    y = uniform.pdf(results[-1], results[0], results[1])

    a.plot(results[-1], y, "b-")

    mean.set(results[3])
    sd.set(results[4])
    areaUpdate.set(results[2] * results[1])

    a.set_xlabel("x")
    a.set_ylabel("y")
    a.set_title("Uniform distribution")

    # For padding
    figureUniform.tight_layout()

    # For filling in areas
    a.fill_between(results[-1], y, alpha = 0.25)

    # Refresh canvas
    canvas.draw()

def areaUniform():
    # Get new lower and upper boundary from sliders
    low = slider1Uniform.get()
    high = slider2Uniform.get()

    areaLow = slider3Uniform.get()
    areaHigh = slider4Uniform.get()
    width = areaHigh-areaLow

    if low > high:
        messagebox.showerror("Value Error", "Value of a should be more than b.")
        return

    # Clear the subplot
    global a
    a.clear()

    # Plot new data into subplot
    results = graph.uniforming(low, high)

    mean.set(results[3])
    sd.set(results[4])
    areaUpdate.set(results[2] * width)

    y = uniform.pdf(results[-1], results[0], results[1])

    a.plot(results[-1], y, "b-")

    a.set_xlabel("x")
    a.set_ylabel("y")
    a.set_title("Uniform distribution")

    # For padding
    figureUniform.tight_layout()

    # For filling in areas
    if areaHigh > high or areaLow < low:
        messagebox.showerror("Value Error", "Area out of range.")
        return
    else:
        area = np.linspace(areaLow, areaHigh, 100)
        a.fill_between(area, results[2], alpha = 0.25)

    # Refresh canvas
    canvas.draw()

ui_frame = Frame(uniform_tab, width = 1280, height = 220, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
ui_frame.place(x = 0, y = 500, width = 1280, height = 220)

slider1UniformLabel = Label(ui_frame, text = "Lower Bound:", font=("Helvetica", 14))
slider1UniformLabel.grid(row=1, column=0, padx=20, sticky="w")

slider1Uniform = Scale(ui_frame, from_ = 1.0, to = 15, orient = HORIZONTAL, resolution = 0.1, length = 300)
slider1Uniform.set(5.0)
slider1Uniform.grid(row=1, column=1, padx=8, sticky = "w",columnspan=2)

slider2UniformLabel = Label(ui_frame, text = "Upper Bound:", font=("Helvetica", 14))
slider2UniformLabel.grid(row=2, column=0, padx=20, sticky="w")

slider2Uniform = Scale(ui_frame, from_ = 1.0, to = 15, orient = HORIZONTAL, resolution = 0.1, length = 300)
slider2Uniform.set(10.0)
slider2Uniform.grid(row=2, column=1, padx=8, sticky = "w",columnspan=2)

uniformButton = Button(ui_frame, text = "Update", bd = 4, width = 10, relief = GROOVE, command = lambda: updateUniform())
uniformButton.grid(row=3, column=0, pady=20, padx=20, sticky = "w")

# CDF Area

slider3UniformLabel = Label(ui_frame, text = "Area Lower Bound:", font=("Helvetica", 14))
slider3UniformLabel.grid(row=1, column=3, padx=20, sticky="w")

slider3Uniform = Scale(ui_frame, from_ = 1.0, to = 15, orient = HORIZONTAL, resolution = 0.1, length = 300)
slider3Uniform.set(5.0)
slider3Uniform.grid(row=1, column=4, padx=8, sticky = "w",columnspan=2)

slider4UniformLabel = Label(ui_frame, text = "Area Upper Bound:", font=("Helvetica", 14))
slider4UniformLabel.grid(row=2, column=3, padx=20, sticky="w")

slider4Uniform = Scale(ui_frame, from_ = 1.0, to = 15, orient = HORIZONTAL, resolution = 0.1, length = 300)
slider4Uniform.set(10.0)
slider4Uniform.grid(row=2, column=4, padx=8, sticky = "w",columnspan=2)

uniformAreaButton = Button(ui_frame, text = "Calculate", bd = 4, width = 10, relief = GROOVE, command = lambda: areaUniform())
uniformAreaButton.grid(row=3, column=3, pady=20, padx=20, sticky = "w")

areaLabel = Label(ui_frame, text = "Area:", font=("Helvetica", 14))
areaLabel.grid(row=3, column=4, padx=20, sticky="w",)

areaNum = Label(ui_frame, textvariable = areaUpdate, font=("Helvetica", 14))
areaNum.grid(row=3, column=5, padx=5, sticky="w")

meanLabel = Label(ui_frame, text = "Mean:", font=("Helvetica", 14))
meanLabel.grid(row=1, column=6, padx=20, sticky="w")

meanNum = Label(ui_frame, textvariable = mean, font=("Helvetica", 14))
meanNum.grid(row=1, column=7, padx=5, sticky="w")

stdLabel = Label(ui_frame, text = "STD:", font=("Helvetica", 14))
stdLabel.grid(row=2, column=6, padx=20, sticky="w")

stdNum = Label(ui_frame, textvariable = sd, font=("Helvetica", 14))
stdNum.grid(row=2, column=7, padx=5, sticky="w")

# * --------------------------------------------------------------- * #

def updateNormal():
    meanNormal = int(meanText.get())
    stdNormal = int(stdText.get())
    trialNormal = int(trialText.get())

    # Clear the subplot
    global b
    b.clear()

    # Plot new data into subplot
    resultNormal = graph.normaling(meanNormal, stdNormal, trialNormal)

    b.hist(resultNormal[1], density = 1)
    b.plot(np.sort(resultNormal[1]), resultNormal[2])

    b.set_xlabel("x")
    b.set_ylabel("y")
    b.set_title("Normal distribution")

    # For padding
    figureNormal.tight_layout()

    # Refresh canvas
    canvasNormal.draw()

# * Normal Distribution initialization
titleNormal = Label(normal_tab, text ='Normal Distribution', font = ("sans-serif", 15, "bold"))
titleNormal.place(x = 550, y = 5)

frameNormal = Frame(normal_tab, width = 1280, height = 500, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
frameNormal.place(x = 0, y = 0, width = 1280, height = 500)

figureNormal = plt.Figure(figsize = (5,4), dpi = 100)
b = figureNormal.add_subplot(1, 1, 1)
meanNormal = 0
stdNormal = 1
rvsNormal = 500

resultNormal = graph.normaling(meanNormal, stdNormal, rvsNormal)

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
ui_frame_normal = Frame(normal_tab, width = 1280, height = 220, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
ui_frame_normal.place(x = 0, y = 500, width = 1280, height = 220)

meanLabel = Label(ui_frame_normal, text = "Mean: ", font=("Helvetica", 14))
meanLabel.grid(row=1, column=0, padx=20, pady= 5, sticky="w")

meanText = Entry(ui_frame_normal, font=("Helvetica", 14))
meanText.grid(row=1, column=1, padx=8, pady= 5, sticky = "w",columnspan=2)

stdLabel = Label(ui_frame_normal, text = "STD: ", font=("Helvetica", 14))
stdLabel.grid(row=2, column=0, padx=20, pady= 5, sticky="w")

stdText = Entry(ui_frame_normal, font=("Helvetica", 14))
stdText.grid(row=2, column=1, padx=8, pady= 5, sticky = "w",columnspan=2)

trialLabel = Label(ui_frame_normal, text = "Trials: ", font=("Helvetica", 14))
trialLabel.grid(row=3, column=0, padx=20, pady= 5, sticky="w")

trialText = Entry(ui_frame_normal, font=("Helvetica", 14))
trialText.grid(row=3, column=1, padx=8, pady= 5, sticky = "w",columnspan=2)

normalButton = Button(ui_frame_normal, text = "Update", bd = 4, width = 10, relief = GROOVE, command = lambda: updateNormal())
normalButton.grid(row=4, column=0, pady=20, padx=20, sticky = "w")

# * Main loop
if __name__ == "__main__":
    root.mainloop()
