from django.urls import path
from usermanagement.views import (RegisterUserAccount
                                  ,OtpPage,LoginUserView
                                  ,LogoutView,
                                  GetUserPostView)

app_name = "user"

urlpatterns =[
    path("register/",RegisterUserAccount.as_view(),name="register-user"),
    path("otp/",OtpPage.as_view(),name="otp-page"),
    path("login/",LoginUserView.as_view(),name="login-user"),
    path("logout/",LogoutView.as_view(),name="logout-user"),
    path("get-user-detail/",GetUserPostView.as_view(),name="get-user-detail")
]