from django.urls import path #Django에서 URL 패턴을 정의하는 함수, 각 URL 요청을 특정 뷰(View)에 연결하는 역할, 이 모듈을 통해 URL과 해당 요청을 처리할 함수(뷰)를 매핑
from posts.views import *

# urlpatterns: Django에서 URL 매핑을 정의하는 필수 변수
# 이 리스트에 정의된 모든 URL과 해당 뷰의 매핑이 프로젝트에 적용
urlpatterns = [
    path('', hello_world, name = 'hello_world'),
    path('page', index, name='my-page'),
    path('intro', intro, name='intro'),
    path('introduction', intro_data, name='intro_data')
]