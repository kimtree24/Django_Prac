from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from posts.models import *

@require_http_methods(["GET"])
def get_post_detail(request,id):
    post = get_object_or_404(Post, pk=id)

    comments = post.comments.all()
    comments_json = [
        {
            "id": comment.id,
            "content": comment.content,
            "writer": comment.writer,
            "created_at": comment.created_at,
        }
        for comment in comments
    ]

    post_detail_json = {
        "id" : post.id,
        "title" : post.title,
        "content" : post.content,
        "writer" : post.writer,
        "category" : post.category,
        "comments" : comments_json,
    }

    return JsonResponse({
        'status' : 200,
        'message' : '게시글 조회 성공',
        'data' : post_detail_json
    })