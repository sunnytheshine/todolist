from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apis import models
from .serializers import TodoSerializer, TodoPATCHSerializer

@api_view(['GET', 'POST'])
def ListTodo(request):
    if request.method == 'GET':
        queryset = models.Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH', 'PUT', 'DELETE'])
def DetailTodo(request, pk, format=None):
    try:
        snippet = models.Todo.objects.get(pk=pk)
    except models.Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = TodoPATCHSerializer(snippet, data=request.data)
        print(request.data)
        if serializer.is_valid() and request.data:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)