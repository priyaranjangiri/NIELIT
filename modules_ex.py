import kagglehub
import pandas as pd

# Download dataset
path = kagglehub.dataset_download("uciml/iris")

print("Dataset downloaded to:", path)

# Load CSV file
df = pd.read_csv(path + "/Iris.csv")

print(df.head())
