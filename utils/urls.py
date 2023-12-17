from django.urls import path
from utils.views import HomeView


app_name = "utils"
urlpatterns = [
    path("",HomeView.as_view(),name="home")
]