from django.contrib import admin
from .models import * #관리자 페이지에 생성한 모델 적용

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)