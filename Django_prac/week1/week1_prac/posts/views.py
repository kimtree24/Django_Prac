from django.shortcuts import render # Django에서 HTML 템플릿을 렌더링(rendering)하는 데 사용되는 함수
from django.http import JsonResponse # 추가
from django.shortcuts import get_object_or_404 # 주어진 모델에서 특정 객체를 가져오고, 객체가 없으면 404 Not Found 오류를 반환, 일반적으로 데이터베이스에서 특정 객체를 조회할 때 사용

# Create your views here.

def hello_world(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
            'data' : "Hello lielion-12th!"
        })

def index(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'intro.html')

def intro_data(request):
    if request.method == "GET":
        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '메시지 전달 성공!',
            'data': [
                {
                    "name": "홍길동",
                    "age": 25,
                    "major": "philosophy"
                },
                {
                    "name": "동길홍",
                    "age": 21,
                    "major": "Economics"
                }
            ]
        })