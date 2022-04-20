from django.urls import path
from .views import userReportView

urlpatterns = [
    path('', userReportView.as_view())
]