from django.urls import path
from .import views

urlpatterns = [
    path("<int:user_id>", views.Todos.as_view()),
    path("<int:user_id>/<int:todo_id>", views.TodosFix.as_view()),
    path("<int:user_id>/<int:todo_id>/check", views.TodoCheck.as_view()),
    path("<int:user_id>/<int:todo_id>/reviews", views.TodoReview.as_view()),
]