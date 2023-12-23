from django.shortcuts import render
from django.views import View
from post.models import Post,Like,Comment,SharedPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from post.forms import PostCreationForm
import json
from utils.utility import get_or_not_found
# from utils.permissions import IsRealLikerUser

class CreatePostView(LoginRequiredMixin,View):
    def post(self,request,*args,**kwargs):
        data = json.loads(request.body)
        form = PostCreationForm(data)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            message = {
                "message":"Post Created Successfully",
                "description":post.description,
                "user": post.user.name
            }
            return JsonResponse({"message":message})
        return JsonResponse({"message":"failed"})
    


class GetAllComments(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        comments = Comment.objects.filter(post__id=id)
        comment = []
        for com in comments:
            dict1 =  {}
            if not com.message:
                continue
            dict1["message"] =com.message
            dict1["user_name"] = com.user.name
            dict1["created_at"] = com.created_at
            comment.append(dict1)

        message = {
            "comment":comment
        }
        return JsonResponse({"message":message})
    


    
class LikeDislikePost(View):
    def get(self,request,*args,**kwargs):
        post = get_or_not_found(Post.objects.all(),id=kwargs.get("id"))
        like , created = Like.objects.get_or_create(post=post,liked_user=request.user)
        if created or not like.is_liked:
            like.is_liked = True
        else :
            like.is_liked=False
        like.save()
        return JsonResponse({"message":post.get_likes})
    
class LikeDislikeSharedPost(View):
    def get(self,request,*args,**kwargs):
        shared_post = get_or_not_found(SharedPost.objects.all(),id=kwargs.get("id"))
        like , created = Like.objects.get_or_create(shared_post=shared_post,liked_user=request.user)
        if created or not like.is_liked:
            like.is_liked = True
        else :
            like.is_liked=False
        like.save()
        return JsonResponse({"message":shared_post.get_likes})