import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.dates import DateFormatter, AutoDateLocator

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

    # Add the download speed plot
    plt.plot(df['Timestamp'], df['Download Speed (Mbps)'], label='Download Speed (Mbps)')

    # Add the upload speed plot
    plt.plot(df['Timestamp'], df['Upload Speed (Mbps)'], label='Upload Speed (Mbps)')

    # Annotate each point with the server location
    for i, row in df.iterrows():
        plt.text(row['Timestamp'], row['Download Speed (Mbps)'], f"{row['Server Location']} - {row['Download Speed (Mbps)']:.2f} Mbps",
                 fontsize=8, ha='left', va='bottom', rotation=45)

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f'Internet Speed Log - {file}')

    # Use AutoDateLocator for automatic date tick placement
    plt.gca().xaxis.set_major_locator(AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

    plt.legend()
    plt.grid(True)

    # Save the figure
    plt.savefig(f'graphs/Graph_log_{time_scale}.png')

    plt.show()
