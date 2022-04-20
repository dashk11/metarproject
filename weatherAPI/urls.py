from django.urls import path
from .Views.metarView import MetarView

urlpatterns = [
    path('', MetarView.as_view())
]
