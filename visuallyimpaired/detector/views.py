from http.client import ResponseNotReady
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DetectModelSerializer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

def index(request):
    return render(request, "detector/index.html")


class DetectView(APIView):

    parser_classes = (MultiPartParser, )

    def get(self,request):
        print(request)
        return Response()

    def post(self,request,*arg, **kwargs):
        
        dSerializer = DetectModelSerializer(data=request.data)
        if (dSerializer.is_valid()):
           dSerializer.save()
        else:
            print(dSerializer.errors)
 
        return Response()
