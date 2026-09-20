import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create unemployment data for India
data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Unemployment Rate": [3.7, 3.5, 3.6, 3.5, 4.8, 8.0, 5.8, 4.2, 4.0]
}

df = pd.DataFrame(data)

print("UNEMPLOYMENT ANALYSIS")
print("====================")

print("\nUnemployment Data:")
print(df)

print("\nBasic Statistics:")
print(df.describe())

# Plot unemployment rate
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=df,
    x="Year",
    y="Unemployment Rate",
    marker="o"
)

plt.title("Unemployment Rate in India")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.tight_layout()

plt.show()