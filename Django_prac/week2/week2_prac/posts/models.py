from django.db import models

# Create your models here.

## 추상 클래스 정의
class BaseModel(models.Model): # 공통 필드 정의하는 추상 클래스 # models.Model class를 상속받아서 BaseModel 구현
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True
    
class Post(BaseModel):

    CHOICES = (
        ('DIARY', '일기'),
        ('STUDY', '공부'),
        ('ETC', '기타')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=20)
    content = models.TextField(verbose_name="내용")
    writer = models.CharField(verbose_name="작성자", max_length=10)
    category = models.CharField(choices=CHOICES, max_length=20)

class Comment(BaseModel):
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name="댓글내용")
    writer = models.CharField(verbose_name="작성자", max_length=10)
    post = models.ForeignKey(
        Post, # 참조할 모델
        on_delete=models.CASCADE, # 게시글 삭제 시 댓글도 삭제
        related_name='comments', # 역참조 이름
        verbose_name='게시글'
    )
