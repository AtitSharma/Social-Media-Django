from django.shortcuts import render
from django.views import View
from post.models import Post,PostImages,Like,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from post.forms import PostCreationForm
import json


# Create your views here.



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
