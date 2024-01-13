from django.urls import path
from usermanagement.views import (RegisterUserAccount
                                  ,OtpPage,LoginUserView
                                  ,LogoutView,
                                  GetUserPostView,
                                  GetAllUserFriendRequest,
                                  AcceptRejectFriendRequest,
                                  GetAllFriendListView 
                                  )

app_name = "user"

urlpatterns =[
    path("register/",RegisterUserAccount.as_view(),name="register-user"),
    path("otp/",OtpPage.as_view(),name="otp-page"),
    path("login/",LoginUserView.as_view(),name="login-user"),
    path("logout/",LogoutView.as_view(),name="logout-user"),
    path("get-user-detail/",GetUserPostView.as_view(),name="get-user-detail"),        
    path("get-all-friend-request/",GetAllUserFriendRequest.as_view(),name="get-all-friend-request"),
    path("accept-reject-friend-request/<int:id>/",AcceptRejectFriendRequest.as_view(),name="accept-reject-friend-request"),
    path("get-all-friends/",GetAllFriendListView.as_view(),name="all-friends")
]