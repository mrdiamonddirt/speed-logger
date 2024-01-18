import speedtest
import time
import datetime
import csv
import os

def speed_test():
    print("Starting speed test...")
    st = speedtest.Speedtest()
    ping = st.get_best_server()['latency']
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    print(f"Ping: {ping:.0f} ms")
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print("Speed test finished.")
    return ping, download_speed, upload_speed

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
            writer.writerow(['Timestamp','Ping (ms)', 'Download Speed (Mbps)', 'Upload Speed (Mbps)'])
        writer.writerow([timestamp, speed_data[0], speed_data[1], speed_data[2]])


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

if __name__ == "__main__":
    interval = int(input("Enter the interval between speed tests in minutes: ")) * 60  # Convert minutes to seconds
    while True:
        speed_data = speed_test()
        log_speed(speed_data)
        print(f"Next test will start in {interval//60} minutes.")
        countdown(interval)