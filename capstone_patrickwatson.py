"""
ISM2411 Capstone — IT Help Desk Tickets Analysis
Author: Patrick Watson
Date:   [Submission Date]

Business Questions:
  1. Which ticket types take longest, and which miss their deadline most?
  2. Which support channel has the happiest clients?
  3. Which day of the week is busiest, and did anything unusual happen in the fall?

AI Disclosure: [fill in at the end]
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)   # create charts/ if it doesn't exist

# ── 1. LOAD ───────────────────────────────────────────────────
data_file = "data/capstone_it_helpdesk.csv"
df = pd.read_csv(data_file)
print("Raw shape:", df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print(df.describe())
print(df["Category"].value_counts())
print("Duplicate rows:", df.duplicated().sum())

# DATA QUALITY ISSUES OBSERVED:
# -
# -
# -