from django.http import JsonResponse
from .models import post
from .serializers import post_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def post_list(request):
    if request.method=='GET':

        posts=post.objects.all()
        serializer=post_serializer(posts,many=True) 
        return JsonResponse({"post":serializer.data},safe=False)
    if request.method=='POST':
        serializer=post_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def post_detail(request,id):
    try:
        Post=post.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=post_serializer(Post)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer=post_serializer(Post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=='DELETE':

        Post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
