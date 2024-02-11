from django.urls import path
from message.views import UserMessageView,UserSocketMessageView


app_name="message"
urlpatterns = [
    path("<int:id>/",UserMessageView.as_view(),name="chats"),
    path("room/",UserSocketMessageView.as_view(),name="enter-room")
]
