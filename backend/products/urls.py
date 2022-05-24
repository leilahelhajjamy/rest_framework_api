from django.urls import path
from .views import *


urlpatterns= [
    path('<int:pk>/',ProductDetailApiView.as_view()),
    path('',ProductListCreateAPIView.as_view()) ,
    path('list' , ProductListAPIView.as_view())

]