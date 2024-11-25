import pandas as pd
import matplotlib.pyplot as plt

# Example data (replace with actual CSV files)
data = {'Year': [2019, 2020, 2021, 2022], 'BondAmount': [100, 200, 300, 400]}
df = pd.DataFrame(data)

# Generate a line plot
plt.figure(figsize=(8, 5))
plt.plot(df['Year'], df['BondAmount'], marker='o')
plt.title("Bond Issuance Over Time")
plt.xlabel("Year")
plt.ylabel("Bond Amount")
plt.grid(True)
plt.show()
