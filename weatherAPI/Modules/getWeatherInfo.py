import requests 
from ..Assets.constants import METAR_STATION_API
import json
from .cacheService import CacheService
from datetime import datetime
import logging 

class WeatherInformation:
    def __init__(self) -> None:
        pass

    def get_weather_info(self, scode, nocache):
        result = {}
        cache_object = CacheService(db_instance=0)
        if cache_object.getKey(scode) and nocache==0:
            result = json.loads(cache_object.getKey(scode))
            result["cache"] = 1
        else:
            response = requests.get(f"https://{METAR_STATION_API}/{scode}")
            station_data = self.extract_weather_info(response.content)
            # Set or overwrite the data
            cache_object.setKey(scode, json.dumps(station_data))
            result = station_data
            result["cache"] = 0
        return result
    
    def extract_weather_info(self, raw_data: bytes) -> dict:
        raw_data = str(raw_data.decode('utf8')).replace("\n", " ").split(" ")
        temperature = raw_data[8].replace("M", "-").split("/")
        field_template = {"station": f"Code is {raw_data[2]}", 
        "last_observation": f"""Last observed at {datetime.strftime(datetime.strptime(raw_data[0]+" "+raw_data[1], "%Y/%m/%d %H:%M"), "%Y-%m-%dT%H:%M:%S")}""", 
        "temperature": f"Temperature is {int(temperature[0])} C and dew point is {int(temperature[1])} C.", 
        "wind": f"Direction {raw_data[5][:3]} and velocity {raw_data[5][3:5]} knots."}
        logging.info("Station raw data: ",raw_data)

        return field_template
        
    

