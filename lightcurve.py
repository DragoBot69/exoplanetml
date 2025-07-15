import pandas as pd
import matplotlib.pyplot as plt

# === Load the .tbl file ===
file_path = "Table.tbl"
df_raw = pd.read_csv(file_path, sep="\t", header=None, engine='python', on_bad_lines='skip')

# === Set headers ===
headers = df_raw.iloc[0]
df = df_raw[1:].copy()
df.columns = headers
df.reset_index(drop=True, inplace=True)

# === Convert columns to numeric ===
columns_to_numeric = [
    "J.D.-2400000", "rel_flux_T1", "rel_flux_err_T1",
    "rel_flux_C2", "rel_flux_C3", "rel_flux_C4",
    "rel_flux_SNR_T1", "FWHM_T1", "Peak_T1"
]

for col in columns_to_numeric:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# === Drop rows with missing time or target flux ===
df = df.dropna(subset=["J.D.-2400000", "rel_flux_T1"])

# === 1. Basic flux vs time ===
plt.figure(figsize=(10, 5))
plt.plot(df["J.D.-2400000"], df["rel_flux_T1"], 'ko-', markersize=3, label="Target Star (T1)")
plt.xlabel("Julian Date (JD - 2400000)")
plt.ylabel("Relative Flux")
plt.title("Light Curve - Target Star (T1)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

# === 2. Light curve with error bars ===
plt.figure(figsize=(10, 5))
plt.errorbar(df["J.D.-2400000"], df["rel_flux_T1"], yerr=df["rel_flux_err_T1"],
             fmt='ko-', ecolor='gray', capsize=2, label="Target Star (T1)")
plt.xlabel("Julian Date (JD - 2400000)")
plt.ylabel("Relative Flux")
plt.title("Light Curve with Error Bars - Target Star (T1)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

# === 3. Comparison star light curves ===
plt.figure(figsize=(10, 5))
plt.plot(df["J.D.-2400000"], df["rel_flux_C2"], 'b.-', label="Comp Star C2")
plt.plot(df["J.D.-2400000"], df["rel_flux_C3"], 'g.-', label="Comp Star C3")
plt.plot(df["J.D.-2400000"], df["rel_flux_C4"], 'r.-', label="Comp Star C4")
plt.xlabel("Julian Date (JD - 2400000)")
plt.ylabel("Relative Flux")
plt.title("Light Curves of Comparison Stars")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

# === 4. SNR of T1 over time ===
plt.figure(figsize=(10, 4))
plt.plot(df["J.D.-2400000"], df["rel_flux_SNR_T1"], 'm.-', label="SNR of T1")
plt.xlabel("Julian Date (JD - 2400000)")
plt.ylabel("SNR")
plt.title("Signal-to-Noise Ratio of T1 Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

# === 5. FWHM of T1 over time ===
plt.figure(figsize=(10, 4))
plt.plot(df["J.D.-2400000"], df["FWHM_T1"], 'c.-', label="FWHM of T1")
plt.xlabel("Julian Date (JD - 2400000)")
plt.ylabel("FWHM (arcsec)")
plt.title("FWHM of T1 Over Time (Seeing Conditions)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

# === 6. Peak value over time ===
plt.figure(figsize=(10, 4))
plt.plot(df["J.D.-2400000"], df["Peak_T1"], 'y.-', label="Peak Pixel Value of T1")
plt.xlabel("Julian Date (JD - 2400000)")
plt.ylabel("Peak Brightness")
plt.title("Peak Counts of T1 Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

# === Final show to keep windows open ===
plt.show()

