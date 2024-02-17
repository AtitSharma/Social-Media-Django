from django.shortcuts import render,redirect
from django.views import View
from usermanagement.forms import UserRegisterForm,OtpVerificationForm,LoginUserForm
from utils.utility import get_or_not_found
from utils.models import OTP
from django.contrib.auth import logout,login,authenticate
from post.models import Post,SharedPost,PostImages
from django.contrib.auth.mixins import LoginRequiredMixin
from usermanagement.models import FriendRequest
from django.db.models import Q
from utils.model_status import Status
from django.http import JsonResponse
from usermanagement.query import GetAllFriendRequestQuery,GetUserAllPostQuery,GetSharedPostQuery
from usermanagement.permissions import IsRealFriendRequestAccepterUser


class RegisterUserAccount(View):
    def post(self,request,*args,**kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            # send_email_to_verify_user(user.id)
            return redirect("user:otp-page")
        return render(request,"user_register.html")
        
    def get(self,request,*args,**kwargs):
        form = UserRegisterForm()
        context = {
            "form":form
        }
        return render(request,"user_register.html",context=context)
    

class OtpPage(View):
    def get(self,request,*args,**kwargs):
        form = OtpVerificationForm()
        return render(request,"otp_verification.html",context={"form":form})
    
    def post(self,request,*args,**kwargs):
        form = OtpVerificationForm(request.POST)
        if form.is_valid():
            user = OTP.objects.filter(otp=form.data.get("otp_code")).first().user
            user.is_active= True
            user.save()
            return redirect("user:login-user")
        return render(request,"otp_verification.html",context={"form":form})
    


class LoginUserView(View):
    def get(self,request,*args,**kwargs):
        form = LoginUserForm()
        return render(request,"user_login.html",context={"form":form})

    def post(self,request,*args,**kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email =  form.data.get("email")
            password = form.data.get("password")
            user = authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect("utils:home")
        return render(request,"user_login.html",context={"form":form})
    

class LogoutView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("user:login-user")
    

class GetUserPostView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.filter(user=request.user).order_by("?")
        shared_posts = SharedPost.objects.filter(user=request.user).order_by("?")
        post_query = GetUserAllPostQuery(data=posts)
        shared_post_query = GetSharedPostQuery(data=shared_posts)

        context = {
            "posts":post_query.get_all_data(),
            "shared_posts":shared_post_query.get_all_data()
        }
        return render(request,"user_profile.html",context=context)
class GetAllUserFriendRequest(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        query = FriendRequest.objects.filter(Q(to_user=request.user) & Q(status=Status.PENDING)).order_by("-created_at")
        data = GetAllFriendRequestQuery(data=query)
        return JsonResponse({"messaage":data.get_all_data()})
        
    

class AcceptRejectFriendRequest(LoginRequiredMixin,IsRealFriendRequestAccepterUser,View):
    def get(self,request,*args,**kwargs):
        friend_request = get_or_not_found(FriendRequest.objects.all(),id=kwargs.get("id"))
        if friend_request.status == Status.ACCEPTED:
            friend_request.status = Status.REJECTED
        if friend_request.status == Status.REJECTED:
            friend_request.status = Status.ACCEPTED
        friend_request.save()
        return JsonResponse({"message":[],"status":200})
    


class GetAllFriendListView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        friends = FriendRequest.objects.filter(to_user=request.user,status=Status.ACCEPTED).all()
        context = {"friends":[]}
        if friends:
            context["friends"] = friends
        return render(request,"friend_request.html",context=context)
        


    


    






    



