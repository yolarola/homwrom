from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blog.models import Post, Product,Category,Shelf,Cell,Arrival,Expenditure
from blog.serializers import PostDVSerializer, PostLVSerializer, UserSerializer,ProductSerializerDV,ProductSerializerLV,ShelfSerializerDV,ShelfSerializerLV,CellSerializerDV,CellSerializerLV,ExpenditureSerializerDV,ExpenditureSerializerLV,ArrivalSerializerDV,ArrivalSerializerLV,CategorySerializerDV,CategorySerializerLV
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
    
    
@csrf_exempt
def category_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializerLV(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializerLV(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializerDV(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializerDV(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)
    

@csrf_exempt
def product_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializerLV(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializerLV(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializerDV(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializerDV(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)
    

@csrf_exempt
def shelf_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        shelf = Shelf.objects.all()
        serializer = ShelfSerializerLV(shelf, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShelfSerializerLV(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shelf_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        shelf = Shelf.objects.get(pk=pk)
    except Shelf.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShelfSerializerDV(shelf)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShelfSerializerDV(shelf, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shelf.delete()
        return HttpResponse(status=204)
    
    
@csrf_exempt
def cell_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        cell = Cell.objects.all()
        serializer = CellSerializerLV(cell, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CellSerializerLV(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cell_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        cell = Cell.objects.get(pk=pk)
    except Cell.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CellSerializerDV(cell)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CellSerializerDV(cell, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cell.delete()
        return HttpResponse(status=204)
    

@csrf_exempt
def arrival_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        arrival = Arrival.objects.all()
        serializer = ArrivalSerializerLV(arrival, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArrivalSerializerLV(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def arrival_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        arrival = Arrival.objects.get(pk=pk)
    except Cell.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArrivalSerializerDV(arrival)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArrivalSerializerDV(cell, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        arrival.delete()
        return HttpResponse(status=204)
    
    
@csrf_exempt
def expenditure_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        expenditure = Expenditure.objects.all()
        serializer = ExpenditureSerializerLV(expenditure, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExpenditureSerializerLV(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def expenditure_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        expenditure = Expenditure.objects.get(pk=pk)
    except Cell.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExpenditureSerializerDV(expenditure)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExpenditureSerializerDV(cell, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        expenditure.delete()
        return HttpResponse(status=204)