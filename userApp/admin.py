from django.contrib import admin
from .models import User #.models는 같은 경로에 있는 파일을 갖고온다는 뜻

# Register your models here.
admin.site.register(User)
