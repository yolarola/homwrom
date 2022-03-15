from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blog.models import Post
from blog.serializers import PostDVSerializer, PostLVSerializer, UserSerializer
from django.contrib.auth.models import User

@csrf_exempt
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def post_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostLVSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostLVSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostDVSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostDVSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)