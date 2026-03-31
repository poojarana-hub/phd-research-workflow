import pandas as pd

# Load data
df = pd.read_csv("data/sample_data.csv")

# Fill missing numeric values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("Data cleaned and saved!")