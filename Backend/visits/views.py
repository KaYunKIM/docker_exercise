from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VisitListSerializer, VisitSerializer
from .models import Visits

# Create your views here.
@api_view(['GET', 'POST'])
def visit(request):
    if request.method=='GET':
        visitors = Visits.objects.all()
        serializer = VisitListSerializer(visitors, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)