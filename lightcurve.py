import pandas as pd
import matplotlib.pyplot as plt

# === Load the .tbl file ===
file_path = "Table.tbl"  # Change path if needed
df_raw = pd.read_csv(file_path, sep="\t", header=None, engine='python', on_bad_lines='skip')

# === Set headers ===
headers = df_raw.iloc[0]
df = df_raw[1:].copy()
df.columns = headers
df.reset_index(drop=True, inplace=True)

# === Convert relevant columns to numeric ===
df["J.D.-2400000"] = pd.to_numeric(df["J.D.-2400000"], errors='coerce')
df["rel_flux_T1"] = pd.to_numeric(df["rel_flux_T1"], errors='coerce')

# === Drop missing data ===
df = df[["J.D.-2400000", "rel_flux_T1"]].dropna()

# === Plot the light curve ===
plt.figure(figsize=(10, 6))
plt.plot(df["J.D.-2400000"], df["rel_flux_T1"], 'ko-', markersize=3, label="Target Star (T1)")
plt.xlabel("Julian Date (JD - 2400000)")
plt.ylabel("Relative Flux")
plt.title("Light Curve of Target Star")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
