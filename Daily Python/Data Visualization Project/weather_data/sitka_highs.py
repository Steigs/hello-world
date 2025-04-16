from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path("/home/steigs/Desktop/PlebDevs/Daily Python/Data Visualization Project/weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract dates and high and low temperatures
dates, highs, lows = [], [],[]
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low Temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)  # Corrected to plot dates on x-axis
ax.plot(dates, lows, color = 'blue', alpha =0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha =0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # This will format the x-axis dates
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
