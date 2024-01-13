from django.urls import path
from post.views import (CreatePostView,
                        LikeDislikePost,
                        LikeDislikeSharedPost,
                        GetAllCommentView,CreateCommentView,
                        GetAllSharedPostCommentView)


app_name = "post"
urlpatterns = [
    path("create-post/",CreatePostView.as_view(),name="create"),
    path("get-all-commets/<int:id>/",GetAllCommentView.as_view(),name="get-all-comments"),
    path("get-all-commets-shared-post/<int:id>/",GetAllSharedPostCommentView.as_view(),name="get-all-comments-shared-post"),
    path("like-dislike-posts/<int:id>/",LikeDislikePost.as_view(),name="like-dislike-posts"),
    path("like-dislike-shared-posts/<int:id>/",LikeDislikeSharedPost.as_view(),name="like-dislike-shared-posts"),
    path("create-comment-post/",CreateCommentView.as_view(),name="create-post-comment")

]