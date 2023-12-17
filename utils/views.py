from django.shortcuts import render
from django.views import View
from post.models import Post

# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        context = {
            "posts" : posts
        }
        return render(request,"home_page.html",context=context)