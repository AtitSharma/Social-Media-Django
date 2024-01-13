from django.shortcuts import render
from django.views import View
from post.models import Post,Like,Comment,SharedPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from post.forms import PostCreationForm,CreatePostCommentForm
import json
from utils.utility import get_or_not_found
from post.query import GetAllCommentsQuery

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
    
    
class LikeDislikePost(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        post = get_or_not_found(Post.objects.all(),id=kwargs.get("id"))
        like , created = Like.objects.get_or_create(post=post,liked_user=request.user)
        if created or not like.is_liked:
            like.is_liked = True
        else :
            like.is_liked=False
        like.save()
        return JsonResponse({"message":post.get_likes})
    
class LikeDislikeSharedPost(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        shared_post = get_or_not_found(SharedPost.objects.all(),id=kwargs.get("id"))
        like , created = Like.objects.get_or_create(shared_post=shared_post,liked_user=request.user)
        if created or not like.is_liked:
            like.is_liked = True
        else :
            like.is_liked=False
        like.save()
        return JsonResponse({"message":shared_post.get_likes})
    


class CreateCommentView(LoginRequiredMixin,View):
    def post(self,request,*args,**kwargs):
        data = json.loads(request.body)
        form = CreatePostCommentForm(data)
        if form.is_valid():
            comment = form.save(user=request.user)
            comment.save()
            return JsonResponse({"message":"Comment Added in Post Successfully ","id":comment.id,"username":comment.user.name,"data":form.data})
        return JsonResponse({"message":"Comment Cannot be Added in Post ","data":[]})


class GetAllCommentView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        post = get_or_not_found(Post.objects.all(),id=kwargs.get("id"))
        data = Comment.objects.filter(post=post).order_by("-created_at")
        comments = GetAllCommentsQuery(data=data)
        return JsonResponse({"message":"All Comments Retrieved Successfully ","data":comments.get_all_data()})
    
    def delete(self,request,*args,**kwargs):

        '''VIEW FOR DELETING COMMENT ON THE BASIS OF COMMENT ID'''
        
        comment = get_or_not_found(Comment.objects.all(),id=kwargs.get("id"))
        comment.delete()
        return JsonResponse({"message":"Comment deleted Succcessfully","data":[]})
    

class GetAllSharedPostCommentView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        shared_post = get_or_not_found(SharedPost.objects.all(),id=kwargs.get("id"))
        data = Comment.objects.filter(shared_post=shared_post).order_by("-created_at")
        comments = GetAllCommentsQuery(data=data)
        return JsonResponse({"message":"All Shared Post Comments Retrieved Successfully ","data":comments.get_all_data()})
    
