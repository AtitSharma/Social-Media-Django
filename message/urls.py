from django.urls import path
from message.views import ListAllMessagesView


app_name="message"
urlpatterns = [
    path("<int:id>/",ListAllMessagesView.as_view(),name="chats")
]
