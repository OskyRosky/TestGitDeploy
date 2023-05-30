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

