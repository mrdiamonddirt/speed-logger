import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 2: Get a list of all CSV files in the 'logs' directory
csv_files = [f for f in os.listdir('logs') if f.endswith('.csv')]

# Step 3: For each CSV file
for file in csv_files:
    # Read the CSV file
    df = pd.read_csv(os.path.join('logs', file))

    # Convert 'Timestamp' to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Extract the time scale
    time_scale = f"{df['Timestamp'].min().strftime('%Y%m%d%H%M%S')}-{df['Timestamp'].max().strftime('%Y%m%d%H%M%S')}"

    # Plot the data
    plt.figure(figsize=(12, 6))

    plt.plot(df['Timestamp'], df['Ping (ms)'], label='Ping (ms)')
    plt.plot(df['Timestamp'], df['Download Speed (Mbps)'], label='Download Speed (Mbps)')
    plt.plot(df['Timestamp'], df['Upload Speed (Mbps)'], label='Upload Speed (Mbps)')

    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title(f'Internet Speed Log - {file}')
    plt.legend()
    plt.grid(True)

    # Save the figure
    plt.savefig(f'graphs/Graph_log_{time_scale}.png')

    plt.show()