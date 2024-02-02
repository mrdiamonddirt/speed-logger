import speedtest
import time
from tqdm import tqdm
import datetime
import csv
import os
import sys

def speed_test():
    print("Starting speed test...")

    # Use tqdm spinner for the speed test
    with tqdm(total=0, position=0, leave=False, dynamic_ncols=True, bar_format='{desc}', file=sys.stdout) as spinner:
        # Step 1: Ping
        spinner.set_description("Getting ping information...")
        time.sleep(1)
        ping = st.get_best_server()['latency']
        spinner.set_description(f"Ping: {ping:.0f} ms")
        spinner.update()

        # Step 2: Server Location
        server_location = st.get_best_server()['name']
        spinner.set_description(f"Server Location - {server_location}, Getting Download speed...")
        spinner.update()

        # Step 3: Download Speed
        download_speed = st.download() / 1024 / 1024  # Convert to Mbps
        spinner.set_description(f"Download Speed - {download_speed:.2f} Mbps, Getting Upload speed...")
        spinner.update()

        # Step 4: Upload Speed
        upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
        spinner.set_description(f"Upload Speed - {upload_speed:.2f} Mbps")
        spinner.refresh()
        time.sleep(1)  # Give a moment to display the final message

    print(f"\nServer location: {server_location}")
    print(f"Ping: {ping:.0f} ms")
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print("Speed test finished.")

    return server_location, ping, download_speed, upload_speed

def log_speed(speed_data):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    foldername = 'logs'
    filename = foldername + '/speed_log_' + datetime.datetime.now().strftime('%Y%m%d') + '.csv'
    
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp','Server Location','Ping (ms)', 'Download Speed (Mbps)', 'Upload Speed (Mbps)'])
        writer.writerow([timestamp, speed_data[0], speed_data[1], speed_data[2], speed_data[3]])


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

if __name__ == "__main__":
    st = speedtest.Speedtest()
    interval = int(input("Enter the interval between speed tests in minutes: ")) * 60  # Convert minutes to seconds
    while True:
        speed_data = speed_test()
        log_speed(speed_data)
        print(f"Next test will start in {interval//60} minutes.")
        countdown(interval)