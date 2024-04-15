import pandas as pd
import matplotlib.pyplot as plt

# Sample data for trends and challenges
data = {
    'Year': [2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Trends': [20, 25, 30, 35, 40, 45, 50],  # Trend scores (e.g., based on surveys)
    'Challenges': [15, 18, 20, 22, 25, 28, 30]  # Challenge scores (e.g., based on industry reports)
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Plotting trends and challenges over the years
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Trends'], marker='o', label='Trends')
plt.plot(df['Year'], df['Challenges'], marker='s', label='Challenges')
plt.title('Developing Trends and Challenges of Digital Forensics')
plt.xlabel('Year')
plt.ylabel('Score')
plt.xticks(df['Year'])
plt.legend()
plt.grid(True)
plt.show()
