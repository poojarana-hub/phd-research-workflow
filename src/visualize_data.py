import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Plot 1: Experiment Score
plt.figure()
df['experiment_score'].plot(kind='bar')
plt.title("Experiment Scores")
plt.savefig("results/score_plot.png")

# Plot 2: Temperature vs Humidity
plt.figure()
plt.scatter(df['temperature'], df['humidity'])
plt.title("Temperature vs Humidity")
plt.savefig("results/temp_humidity.png")

print("Plots saved!")