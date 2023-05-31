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


### Test 3

import matplotlib.pyplot as plt

# Create a list of years
years = list(range(1923, 2023))

# Create a list of values
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Plot the line
plt.plot(years, values)

# Add a title
plt.title("Plot Line with 100 Years")

# Add labels to the axes
plt.xlabel("Years")
plt.ylabel("Values")

# Show the plot
plt.show()

plt.plot(years, values, linestyle="--", color="red", linewidth=2)

plt.plot(years, values, label="Values")
plt.legend()

plt.savefig("plot.png")




############################### Último código o etapa

import pandas as pd

# Create a list of dictionaries to store the data
data = [{'Name': 'John', 'Age': 25, 'Country': 'United States'},
        {'Name': 'David', 'Age': 27, 'Country': 'Canada'},
        {'Name': 'Michael', 'Age': 30, 'Country': 'United Kingdom'}]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Print the DataFrame
print(df)