import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df=pd.read_csv("Crop_recommendation.csv")

# Define percentiles for categorization
low_threshold = df['N'].quantile(0.33)
high_threshold = df['N'].quantile(0.67)

# Create a new column 'N_category' based on the thresholds
df['N_category'] = pd.cut(df['N'], bins=[-float('inf'), low_threshold, high_threshold, float('inf')],
                          labels=['Low', 'Moderate', 'High'], include_lowest=True)
# Define percentiles for categorization
low_threshold = df['K'].quantile(0.33)
high_threshold = df['K'].quantile(0.67)

# Create a new column 'N_category' based on the thresholds
df['K_category'] = pd.cut(df['K'], bins=[-float('inf'), low_threshold, high_threshold, float('inf')],
                          labels=['Low', 'Moderate', 'High'], include_lowest=True)

# Display the updated DataFrame

# Define percentiles for categorization
low_threshold = df['P'].quantile(0.33)
high_threshold = df['P'].quantile(0.67)

# Create a new column 'N_category' based on the thresholds
df['P_category'] = pd.cut(df['P'], bins=[-float('inf'), low_threshold, high_threshold, float('inf')],
                          labels=['Low', 'Moderate', 'High'], include_lowest=True)


