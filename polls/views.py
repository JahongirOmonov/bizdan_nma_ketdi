from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import todoModel
from .serializer import TodoSerializer
from rest_framework import status
import datetime

# Create your views here.


class getall(APIView):
    def get(self, request):
        some = todoModel.objects.all()
        serializer = TodoSerializer(some, many=True)
        return Response(serializer.data)
    
class getdetail(APIView):
    def get(self, request, *args, **kwargs):
        x=get_object_or_404(todoModel, id=kwargs['forid'])
        serializer=TodoSerializer(x)
        return Response(serializer.data)
    
class post(APIView):
    def post(self, request):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class patch(APIView):
    def patch(self, request, *args, **kwargs):
        x=get_object_or_404(todoModel, id=kwargs['forid'])
        serializer=TodoSerializer(x, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class put(APIView):
    def put(self, request, *args, **kwargs):
        x=get_object_or_404(todoModel, id=kwargs['forid'])
        c=TodoSerializer(x, data=request.data)
        if c.is_valid():
            c.save()
            return Response(c.data)
        return Response(c.errors)
    
class delete(APIView):
    def delete(self, request, *args, **kwargs):
        x=get_object_or_404(todoModel, id=kwargs['forid'])
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class today(APIView):
    def get(self, request, *args, **kwargs):
        today=datetime.date.today()
        x=todoModel.objects.filter(create_at__date=today)
        serializer=TodoSerializer(x, many=True)
        return Response(serializer.data)
    
class last_ten(APIView):
    def get(self, request, *args, **kwargs):
        today=datetime.datetime.now()
        last_ten=today-datetime.timedelta(days=10)
        x=todoModel.objects.filter(create_at__gte=last_ten, create_at__lte=today)
        ser=TodoSerializer(x, many=True)
        return Response(ser.data)
    
class status(APIView):
    def get(self, request, *args, **kwargs):
        today=datetime.date.today()
        x=todoModel.objects.filter(create_at__date=today, status=True)
        ser=TodoSerializer(x, many=True)
        return Response(ser.data)


