from django.contrib.auth.models import User, Group
from requests import Response
from .serializers import WordSerializer
from rest_framework import status
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from .models import Word
from rest_framework.schemas import AutoSchema

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .stubs import list_stub, normalize_dict


@csrf_exempt
@api_view(['GET','POST'])
def word_list(request):
    if request.method == 'GET':
        word = Word.objects.all()
        serializer = WordSerializer(word,many = True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    elif request.method == 'POST':
        serializer = WordSerializer(data = request.data)      
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def word_stubs(request,pk):
    """
    Stubbed View to top 100 normalized words
    * Public
    """
    if request.method == 'GET':
        return Response(normalize_dict(list_stub[pk]))