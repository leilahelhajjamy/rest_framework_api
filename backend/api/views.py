from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import  ProductSerializer
from django.http import JsonResponse
# Create your views here.

@api_view(["GET","POST"])
def api_home(request, *args , **kwargs):

   serializer = ProductSerializer(data = request.data)
   if serializer.is_valid():
       print(serializer.data)
      # instance = serializer.save()

       return Response(serializer.data)
