
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .models import Todo
from .serializers import TodoSerializer


class ListAllTodosView(APIView):

    permission_classes = [AllowAny]
    # authentication_classes = [TokenAuthentication]

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class ListUserTodoView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        if request.user.is_staff:
            data = Todo.objects.all()
        else:
            data = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("Todo created successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk, user):
        return Todo.objects.filter(id=pk, user=user).first()

    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        data = Todo.objects.get(id=id, user=request.user)
        if not data:
            return Response(
                {"error": "You are not allowed to access this todo"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = TodoSerializer(data)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        id = kwargs.get("pk")
        todo = Todo.objects.get(id=id, user=request.user)
        if not todo:
            return Response(
                {"error": "You are not allowed to access this todo"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        id = kwargs.get("pk")
        todo = Todo.objects.get(id=id, user=request.user)
        if not todo:
            return Response(
                {"error": "You are not allowed to access this todo"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        id = kwargs.get("pk")
        todo = Todo.objects.get(id=id, user=request.user)
        if not todo:
            return Response(
                {"error": "You are not allowed to access this todo"},
                status=status.HTTP_403_FORBIDDEN
            )
        todo.delete()
        return Response("Todo Removed", status=status.HTTP_202_ACCEPTED)


class CompletedTodoListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        todos = Todo.objects.filter(completed=True)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


# token: "e63acfb392345cd6895cbb0b22f3f1ed9a5bd5a0"
