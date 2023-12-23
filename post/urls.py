from django.urls import path
from post.views import CreatePostView,GetAllComments,LikeDislikePost,LikeDislikeSharedPost


app_name = "post"
urlpatterns = [
    path("create-post/",CreatePostView.as_view(),name="create"),
    path("get-all-commets/<int:id>/",GetAllComments.as_view(),name="get-all-comments"),
    path("like-dislike-posts/<int:id>/",LikeDislikePost.as_view(),name="like-dislike-posts"),
    path("like-dislike-shared-posts/<int:id>/",LikeDislikeSharedPost.as_view(),name="like-dislike-shared-posts"),

]