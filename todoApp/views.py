from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import Todo, User
from .serializers import TodoSerializer

class Todos(APIView):

    def get_user(self,user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user
    
    def get_todo(self,user_id,todo_id):
        user = self.get_user(user_id)
        try:
            todo = Todo.objects.get(id = todo_id)
        except Todo.DoesNotExist:
            raise NotFound("To Do를 찾을 수 없습니다.")
        return todo
    
    def get(self, request, user_id):
        now = timezone.localtime(timezone.now())
        current_month = now.month
        current_day = now.day

        month = request.query_params.get("month",current_month)
        month = int(month)

        day = request.query_params.get("day", current_day)
        day = int(day)

        user = self.get_user(user_id)
        todos = Todo.objects.filter(
            date__month = month,
            date__day = day,
            user = user
        )
        serializer = TodoSerializer(
            todos,
            many = True
        )
        return Response(serializer.data)
    
    def post(self, request, user_id):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_user(user_id)
            serializer.save(
                user = user
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class TodosFix(APIView):
    def get_user(self,user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user
    
    def get_todo(self,user_id,todo_id):
        user = self.get_user(user_id)
        try:
            todo = Todo.objects.get(id = todo_id)
        except Todo.DoesNotExist:
            raise NotFound("To Do를 찾을 수 없습니다.")
        return todo
    def patch(self, request, user_id, todo_id):
        todo = self.get_todo(user_id,todo_id)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, user_id, todo_id):
        todo = self.get_todo(user_id, todo_id)
        todo.delete()
        return Response({'message': '삭제 성공'})

class TodoCheck(APIView):
    def get_user(self,user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user
    
    def get_todo(self,user_id,todo_id):
        user = self.get_user(user_id)
        try:
            todo = Todo.objects.get(id = todo_id)
        except Todo.DoesNotExist:
            raise NotFound("To Do를 찾을 수 없습니다.")
        return todo
    def patch(self, request, user_id, todo_id):
        todo = self.get_todo(user_id, todo_id)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class TodoReview(APIView):
    def get_user(self,user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
        return user
    
    def get_todo(self,user_id,todo_id):
        user = self.get_user(user_id)
        try:
            todo = Todo.objects.get(id = todo_id)
        except Todo.DoesNotExist:
            raise NotFound("To Do를 찾을 수 없습니다.")
        return todo
    def patch(self, request, user_id, todo_id):
        todo = self.get_todo(user_id, todo_id)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)