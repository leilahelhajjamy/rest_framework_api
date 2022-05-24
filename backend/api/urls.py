from django.urls import path
from .views import *



urlpatterns = [
    path('' , api_home) # don't forget again, no parameters passed
]