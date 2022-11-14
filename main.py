import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

filename = 'temps.csv'

times = []
light = []
temps = {
    "temp1": [],
    "temp2": [],
    "temp3": [],
    "temp4": [],
    "temp5": [],
    "temp6": [],
    "temp7": [],
    "temp8": [],
    "temp9": []
}
# Load the data
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        if line == '':
            continue
        parts = line.split(',')
        if (float(parts[2]) < -10 or
            float(parts[3]) < -10 or
            float(parts[4]) < -10 or
            float(parts[5]) < -10 or
            float(parts[6]) < -10 or
            float(parts[7]) < -10 or
            float(parts[8]) < -10 or
            float(parts[9]) < -10 or
            float(parts[10]) < -10):
            continue
        times.append(mdates.date2num(datetime.strptime(parts[0].replace("-", "/"), '%Y/%m/%d/%H:%M:%S.%f')))
        light.append(parts[1])
        temps["temp1"].append(float(parts[2]))
        temps["temp2"].append(float(parts[3]))
        temps["temp3"].append(float(parts[4]))
        temps["temp4"].append(float(parts[5]))
        temps["temp5"].append(float(parts[6]))
        temps["temp6"].append(float(parts[7]))
        temps["temp7"].append(float(parts[8]))
        temps["temp8"].append(float(parts[9]))
        temps["temp9"].append(float(parts[10]))

# Convert the data to numpy arrays
times = np.array(times)
light = np.array(light)
temps["temp1"] = np.array(temps["temp1"])
temps["temp2"] = np.array(temps["temp2"])
temps["temp3"] = np.array(temps["temp3"])
temps["temp4"] = np.array(temps["temp4"])
temps["temp5"] = np.array(temps["temp5"])
temps["temp6"] = np.array(temps["temp6"])
temps["temp7"] = np.array(temps["temp7"])
temps["temp8"] = np.array(temps["temp8"])
temps["temp9"] = np.array(temps["temp9"])
fig, ax1 = plt.subplots()
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature')
ax1.set_title('Temperature over time')

ax1.plot(times, temps["temp1"], label="temp1")
ax1.plot(times, temps["temp2"], label="temp2")
ax1.plot(times, temps["temp3"], label="temp3")
ax1.plot(times, temps["temp4"], label="temp4")
ax1.plot(times, temps["temp5"], label="temp5")
ax1.plot(times, temps["temp6"], label="temp6")
ax1.plot(times, temps["temp7"], label="temp7")
ax1.plot(times, temps["temp8"], label="temp8")
ax1.plot(times, temps["temp9"], label="temp9")

ax2 = ax1.twinx()
ax2.set_ylabel('Light')
ax2.plot(times, light, label="light", linestyle='--', color='black', linewidth=0.2)
plt.show()