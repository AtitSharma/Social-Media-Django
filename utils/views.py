from django.shortcuts import render
from django.views import View
from post.models import Post
from utils.permissions import LogindInUserView
from usermanagement.query import GetUserAllPostQuery



class HomeView(LogindInUserView):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all().order_by("?")
        query = GetUserAllPostQuery(data=posts)
        context = {
            "posts" : query.get_all_data()
        }
        return render(request,"home_page.html",context=context)
    


def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_403(request, exception):
    return render(request, '403.html', status=403)

def error_500(request):
    return render(request, '500.html', status=500)