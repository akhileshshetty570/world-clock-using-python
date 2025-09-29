from datetime import datetime, timedelta
import pytz

utc_time = datetime.now(pytz.utc)
print("UTC         :", utc_time.strftime("%Y-%m-%d %H:%M"))

cities  = ["Los Angeles", "New York", "London", "Paris", "Dubai", "India", "Singapore", "Tokyo", "Sydney", "Wellington"]
offsets = [-7, -4, 1, 1, 4, 5.5, 8, 9, 10, 12]  

for i in range(len(cities)):
    hours = int(offsets[i])
    minutes = int((offsets[i] - hours) * 60) 
    city_time = utc_time + timedelta(hours=hours, minutes=minutes)
    print(f"{cities[i]:<12}: {city_time.strftime('%Y-%m-%d %H:%M')}")