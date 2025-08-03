
import pandas as pd
input_data = {"english": 40, "maths": 50,"tamil":60}

df1 = pd.DataFrame.from_dict(input_data, orient='index', columns=['Score'])
print("DataFrame Method 1 (orient='index'):\n", df1)
print("\n")
s = pd.Series(input_data)
df4 = s.to_frame(name='Score') # Convert Series to DataFrame with a specific column name
print("DataFrame Method 4 (via Series to_frame):\n", df4)
print("\n")
df3 = pd.DataFrame([input_data]) # Wrap the dictionary in a list to make it a single row
print("DataFrame Method 3 (wrapped in list):\n", df3)

print("\n")
