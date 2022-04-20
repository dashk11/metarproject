from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserReport
from .serializer import UserReportSerialzier
# Create your views here.

class userReportView(APIView):
    def get(self, request):
        try:
            print(request.data)
            qs = UserReport.objects.all()
            # No additional database hits required
            result = UserReportSerialzier(qs, many=True).data
            return Response({"data": result})

        except Exception as error:
            print(error)
            return Response({"Message": "An exception has occurred."})