import pandas as pd
import os

# path to logs file
log_path = "output/logs.csv"

# read logs
df = pd.read_csv(log_path)

# extract date from timestamp
df['date'] = df['timestamp'].str[:10]

# group by date and vehicle type
date_report = df.groupby(['date', 'vehicle_type']).size().reset_index(name='count')

# save report
output_path = "output/date_wise_report.csv"
date_report.to_csv(output_path, index=False)

print("✅ Date-wise vehicle report saved at:", output_path)
