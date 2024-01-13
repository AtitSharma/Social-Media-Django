from django.urls import path
from message.views import UserMessageView


app_name="message"
urlpatterns = [
    path("<int:id>/",UserMessageView.as_view(),name="chats")
]
