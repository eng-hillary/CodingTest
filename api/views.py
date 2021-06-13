from django.shortcuts import render

# Create your views here.
from .serializers import ProductSerializer, PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from posts.models import Post

@api_view(['GET'])
def ProductList(request):
    productlist = Product.objects.all()
    serializer = ProductSerializer(productlist, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PostList(request):
    postlist = Post.objects.all()
    serializer = PostSerializer(postlist, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ProductDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def PostDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ProductCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
    

@api_view(['POST'])
def PostCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(['POST'])
def ProductUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def PostUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def ProductDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('product deleted successfully')

@api_view(['DELETE'])
def PostDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response('post deleted successfully')







