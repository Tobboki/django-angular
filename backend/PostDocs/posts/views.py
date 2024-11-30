from django.http import JsonResponse
from .models import Post,User,comment
from .serializers import post_serializer,User_serializer,comment_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# def userfa():

#     url='https://jsonplaceholder.typicode.com/posts'
#     response=requests.get(url)

#     posts=response.json()
#     for i in posts:
#             user_instance =User.objects.get(id=i['userId'])
      
#             post, created = Post.objects.get_or_create(
#                 title=i['title'],
#                 content=i['body'],
                
#                 user=user_instance
#                 )

@api_view(['GET','POST'])
def post_list(request):
    if request.method=='GET':
        # userfa()

        posts=Post.objects.all()
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
        Post1=Post.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=post_serializer(Post1)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer=post_serializer(Post1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=='DELETE':

        Post1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


 
# def userfa():

#         url='https://jsonplaceholder.org/users'
#         response=requests.get(url)
    
        
#         users=response.json()

#         for i in users:
                
        
#                 user, created = User.objects.get_or_create(
#                     firstname=i['firstname'],
#                     lastname=i['lastname'],
                    
#                     email=i['email'])
            
@api_view(['GET', 'POST'])
def User_list(request):
    if request.method=='GET':
        # userfa()

        Users=User.objects.all()
        serializer=User_serializer(Users,many=True) 
        return JsonResponse({"user":serializer.data},safe=False)
    if request.method=='POST':
        serializer=User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request,id):
    try:
        User1=User.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=User_serializer(User1)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer=User_serializer(User1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=='DELETE':

        User1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


def userfa():

    url='https://jsonplaceholder.org/comments'
    response=requests.get(url)
   
    if response.status_code == 200:
        posts=response.json()
        for i in posts:
            
                
            user_instance =User.objects.get(id=i['userId'])
            post_instance =Post.objects.get(id=i['postId'])
            
           
            post, created = comment.objects.get_or_create(
                content=i['comment'],
                post=post_instance,
                
                user=user_instance  )
@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method=='GET':
        userfa()

        comments=comment.objects.all()
        serializer=comment_serializer(comments,many=True) 
        return JsonResponse({"comments":serializer.data},safe=False)
    if request.method=='POST':
        serializer=comment_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request,id):
    try:
        comment1=comment.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=comment_serializer(comment1)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer=comment_serializer(comment1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=='DELETE':

        comment1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    