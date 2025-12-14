from django.urls import path
from .views import power

urlpatterns = [
    path("power/", power, name="power"),
]
