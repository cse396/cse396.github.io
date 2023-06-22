import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import time

fig, ax = plt.subplots()
plt.ion()

def create_data():
    data = {
        'distance': {},
        'radius': {}
    }

    for i in range(361):
        data['distance'][int(i)] = 0.0
        data['radius'][int(i)] = i

    with open("distance.txt", "w") as file:
        file.write(str(data))

def update_robot_position(movement, df):
    if movement == -1:
        return df  # Move on without making any updates

    old_df = df.copy()  # Create a copy of the current DataFrame

    if movement.startswith('L'):
        distance = int(movement[1:])
        df['radius'] = (df['radius'] + distance) % 360
    elif movement.startswith('R'):
        distance = int(movement[1:])
        df['radius'] = (df['radius'] - distance) % 360
    elif movement.startswith('U'):
        distance = int(movement[1:])
        df['distance'] += distance
    elif movement.startswith('D'):
        distance = int(movement[1:])
        df['distance'] -= distance

    # Preserve the old values in the global map
    df['distance'] = np.where(df['distance'] == 0, old_df['distance'], df['distance'])
    df['radius'] = np.where(df['radius'] == 0, old_df['radius'], df['radius'])

    return df

create_data()

while True:
    degree = 0
    with open("degree.txt", "r") as file:
        degree = file.read()

    if degree == "" or not degree.isdigit() or int(degree) > 180 or int(degree) < 0:
        print(f"degree is not valid: {degree}")
        time.sleep(0.5)
        continue

    sonic1 = 0
    with open("distanceSonic1.txt", "r") as file:
        sonic1 = file.read()

    sonic2 = 0
    with open("distanceSonic2.txt", "r") as file:
        sonic2 = file.read()

    sonic2 = float(sonic2)

    with open("distance.txt", "r") as file:
        data = file.read().replace('\n', '')

    data = ast.literal_eval(data)

    df = pd.DataFrame.from_dict(data)

    # Read robot movement from robot.txt and update the global map
    with open("robot.txt", "r") as file:
        robot_movement = file.read()

    df = update_robot_position(int(robot_movement), df)

    df.loc[int(degree), "distance"] = float(sonic1)
    df.loc[int(degree) + 180, "distance"] = float(sonic2)

    x = df["distance"] * np.cos(np.deg2rad(df["radius"]))
    y = df["distance"] * np.sin(np.deg2rad(df["radius"]))

    plotData = pd.DataFrame(columns=["x", "y"])
    plotData["x"] = x
    plotData["y"] = y

    with open("distance.txt", "w") as file:
        file.write(str(df.to_dict()))

    ax.clear()
    ax.scatter(plotData["x"], plotData["y"])
    plt.draw()
    plt.pause(0.01)
    time.sleep(0.5)
