from datetime import datetime, timedelta
from random import uniform
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time

# Set your InfluxDB connection parameters
url = ""
token = ""
org = ""
bucket = "s"

# Initialize InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Function to generate simulated sensor data
def generate_sensor_data():
    timestamp = datetime.utcnow()
    temperature = uniform(20, 30)  # Simulated temperature data (between 20°C and 30°C)
    humidity = uniform(40, 60)     # Simulated humidity data (between 40% and 60%)
    return timestamp, temperature, humidity

# Insert simulated sensor data into InfluxDB
for i in range(100):  # Insert 100 data points
    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    timestamp, temperature, humidity = generate_sensor_data()
    
    # Create InfluxDB data point
    point = Point("sensor_data") \
        .tag("sensor",  "sensor_1") \
        .field("temperature", temperature) \
        .field("humidity", humidity) \
        .time(timestamp, WritePrecision.NS)
    
    # Write data point to InfluxDB
    write_api.write(bucket=bucket, org=org, record=point)
    if i % 10 == 0:
        time.sleep(10)
    else:
        time.sleep(300)

print("Data inserted successfully.")