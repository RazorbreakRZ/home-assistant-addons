import os, time, random
import schedule
from influxdb import InfluxDBClient
import pandas as pd

print("App started")

def job():
    print("Started InfluxDB client")
    spreadsheet = os.environ.get("SPREADSHEET_ID","1lcpYabMhygGCH4n5jVwKThVvcrvwTtJfd_pcNla4vss")
    sheet = os.environ.get("SHEET_ID","28991115")
    df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{spreadsheet}/export?format=csv&gid={sheet}')
    points = []
    for zone,deposit,level in df.itertuples(index=False, name='water'):
        point = {
            "measurement": "water",
            "tags": {
                "zone": zone,
                "deposit": deposit
            },
            "fields": {
                "level": level
            }
        }
        print(point)
        points.append(point)
    client = InfluxDBClient('192.168.8.99', 8086, 'influxdb_user', 'influxdb_user', 'la-farga')
    client.write_points(points, retention_policy='weekly')
    client.close()
    print("Stopped InfluxDB client")

schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(15)