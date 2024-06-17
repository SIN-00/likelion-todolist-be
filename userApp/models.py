from django.db import models

# Create your models here.

class User(modes.Model) :
    username = models.CharField(
        max_length = 150,
        unique=True
    )
    password = models.CharField(
        max_length = 150,
    )
def __str__(self): #유저클래스를 문자열로 바꿔야할 있을때
    return self.username #유저클래스를 대표하는 문자열 