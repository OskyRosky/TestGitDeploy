# Test 

import pandas as pd
import numpy as np

# Create a DatetimeIndex of 100 random dates
dates = pd.date_range('2023-05-30', periods=100, freq='D')

# Create a NumPy array of 100 random energy values
energy = np.random.randint(0, 100, 100)

# Create a DataFrame with the date, time, and energy columns
df = pd.DataFrame({'date': dates, 'time': dates.time, 'energy': energy})

# Print the DataFrame
print(df)

###### 

# Test 2: barchart

import matplotlib.pyplot as plt
import numpy as np

# Generate the simulated data
data = np.random.randint(0, 100, (10, 2))

# Create a bar chart
plt.bar(data[:, 0], data[:, 1], color="blue")

# Plot the bar chart
plt.show()

import seaborn as sns

# Generate the simulated data
data = np.random.randint(0, 100, (10, 2))

# Create a bar chart
sns.barplot(x=data[:, 0], y=data[:, 1])

# Plot the bar chart
plt.show()

import pandas as pd

# Generate the simulated data
data = pd.DataFrame({"A": np.random.randint(0, 100, (10,)), "B": np.random.randint(0, 100, (10,))})

# Create a bar chart
data.plot.bar(x="A", y="B")

# Plot the bar chart
plt.show()


#### Test 3

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({"Dog Name": ["Scooby-Doo", "Simba", "Laika"], "Owner": ["Fred", "Scar", "Yuri"], "Resident State": ["California", "Florida", "New York"]})

# Print the DataFrame
print(df)
