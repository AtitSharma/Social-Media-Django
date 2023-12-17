from django.urls import path
from post.views import CreatePostView,GetAllComments


app_name = "post"
urlpatterns = [
    path("create-post/",CreatePostView.as_view(),name="create"),
    path("get-all-commets/<int:id>/",GetAllComments.as_view(),name="get-all-comments")
]