from datetime import date
from rest_framework import serializers
import pandas as pd

class QueryParamSerializer(serializers.Serializer):
    scode = serializers.CharField(max_length=10)
    nocache = serializers.BooleanField()
    
    def validate(self, data):
        df = pd.read_csv(r'weatherAPI/Assets/stations.csv')
        valid_stations = list(df["STATIONS"])
        if data['scode'] not in valid_stations:
            raise serializers.ValidationError("Invalid Scode")
        return data