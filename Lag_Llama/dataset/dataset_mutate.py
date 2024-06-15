import sys
import pandas as pd

if len(sys.argv) > 2:
    file = sys.argv[1]
    new_file = sys.argv[2]
else:
    raise ValueError("No input csv file")

print(f"input csv file: {file}")

# 读取 CSV 文件，不加索引行
df = pd.read_csv(file)

# List of cities
cities = ['City1', 'City2', 'City3', 'City4', 'City5', 'City6', 'City7', 'City8', 'City9', 'City10', 'City11', 'City12']

# Duplicate each row for each city using list comprehension
rows = [row.tolist()[0:1] + [city] + row.tolist()[1:] for _, row in df.iterrows() for city in cities]

# Create new DataFrame from rows with 'City' as the second column
column_names = df.columns.tolist()
column_names.insert(1, 'City')
df_new = pd.DataFrame(rows, columns=column_names)
df_new.columns.values[0] = None

# Save the new DataFrame to a CSV file
df_new.to_csv(new_file, index=False)

