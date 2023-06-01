import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import time

fig, ax = plt.subplots()
plt.ion()

while True:
    degree = 0
    with open("degree.txt", "r") as file:
        degree = file.read()
    
    sonic1 = 0
    with open ("distanceSonic1.txt", "r") as file:
        sonic1 = file.read()

    sonic2 = 0 
    with open ("distanceSonic2.txt", "r") as file:
        sonic2 = file.read()
    
    sonic2 = float(sonic2)
    sonic2 += 180

    df = pd.DataFrame(np.zeros((360, 2)), columns=["distance", "radius"])
    
    df["radius"][int(degree)] = float(sonic1)
    df["radius"][int(degree) + 180] = float(sonic2)
    
    x = df["distance"] * np.cos(np.deg2rad(df["radius"]))
    y = df["distance"] * np.sin(np.deg2rad(df["radius"]))

    plotData = pd.DataFrame(columns=["x", "y"]) 
    plotData["x"] = x
    plotData["y"] = y

    ax.clear()  # Clear the previous plot
    ax.scatter(plotData["x"], plotData["y"])
    plt.draw()
    plt.pause(0.01)
    time.sleep(0.5)