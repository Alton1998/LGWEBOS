from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Heart
from .serializer import HeartSerializer

class HeartAPIView(APIView):
    def get(self, request):
        data= Heart.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer = HeartSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.