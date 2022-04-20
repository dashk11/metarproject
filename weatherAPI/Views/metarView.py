from rest_framework.views import APIView
from rest_framework.response import Response
from ..Serializers.queryParamSerializer import QueryParamSerializer
from ..Modules.getWeatherInfo import WeatherInformation
from ..Modules.cacheService import CacheService

class MetarView(APIView):
    def get(self, request):
        try:
            serializer = QueryParamSerializer(data=request.query_params)
            serializer.is_valid(raise_exception=True)
            weather_info_obj = WeatherInformation()
            details = weather_info_obj.get_weather_info(
                scode=serializer.data["scode"],
                nocache=serializer.data["nocache"])
            return Response(details)

        except Exception as error:
            return Response({"Message": "An exception has occurred."})
