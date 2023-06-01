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
    
    with open ("distance.txt", "r") as file:
        data = file.read().replace('\n', '')
    data = ast.literal_eval(data)

    df = pd.DataFrame.from_dict(data) 

    #for i in range(0, 360):
    #    df.loc[i, "distance"] = 0


    df.loc[int(degree), "distance"] = float(sonic1)
    df.loc[int(degree) + 180, "distance"] = float(sonic2)


    x = df["distance"] * np.cos(np.deg2rad(df["radius"]))
    y = df["distance"] * np.sin(np.deg2rad(df["radius"]))

    plotData = pd.DataFrame(columns=["x", "y"]) 
    plotData["x"] = x
    plotData["y"] = y

    with open("distance.txt", "w") as file:
        file.write(str(df.to_dict()))

    ax.clear()  # Clear the previous plot
    ax.scatter(plotData["x"], plotData["y"])
    plt.draw()
    plt.pause(0.01)
    time.sleep(0.5)