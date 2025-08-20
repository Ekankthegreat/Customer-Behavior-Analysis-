import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
n = 100
data = pd.DataFrame({
    "Acquisition_Cost": np.random.uniform(50, 500, n),
    "Lifetime_Value": np.random.uniform(200, 5000, n),
    "Segment": np.random.choice(["A", "B", "C"], n)
})

# Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Plot
plt.figure(figsize=(8, 8))  # 512x512 with dpi=64
sns.scatterplot(
    data=data,
    x="Acquisition_Cost",
    y="Lifetime_Value",
    hue="Segment",
    palette="Set2",
    s=80,
    edgecolor="black"
)

plt.title("Customer Lifetime Value vs. Acquisition Cost", fontsize=16)
plt.xlabel("Acquisition Cost ($)")
plt.ylabel("Customer Lifetime Value ($)")
plt.tight_layout()

# Save
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
