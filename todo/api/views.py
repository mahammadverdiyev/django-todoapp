from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import generics

# generic class based views


class TodosApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# class TodosApiView(APIView):
#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TodoSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class TodoDetailApiView(APIView):
#     def get_object(self, id):
#         todo = get_object_or_404(Todo, id=id)
#         return todo

#     def get(self, request, id):
#         todo = self.get_object(id)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)

#     def put(self, request, id):
#         todo = self.get_object(id)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         todo = self.get_object(id)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
