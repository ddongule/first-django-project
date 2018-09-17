from django.contrib import admin
from .models import Post # 아까 정의했던 Post 모델을 가져오고 있음
# Register your models here.

admin.site.register(Post) #올리지 않으면 admin에 들어가도 나오지 않는다
