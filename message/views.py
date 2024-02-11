from django.shortcuts import render
from django.http import JsonResponse
from utils.permissions import LogindInUserView
from utils.utility import get_or_not_found
from message.models import Message
from usermanagement.models import User
from message.query import MessageQuery
from django.db.models import Q
from django.core.exceptions import PermissionDenied


class UserMessageView(LogindInUserView):
    def get(self,request,*args,**kwargs):

        ''' Requires user id to get all messages'''

        to_user = get_or_not_found(User.objects.all(),id=kwargs.get("id"))
        messages = Message.objects.filter(Q(Q(from_user=request.user) & Q(to_user=to_user)) | Q(Q(from_user=to_user) & Q(to_user=request.user))).order_by("created_at")
        query = MessageQuery(messages)
        return JsonResponse({"message":"All Chat History Retrieved Successfully","data":query.get_all_data()})
    
    def delete(self,request,*args,**kwargs):

        ''' Requires Message id in order to delete the message '''

        message = get_or_not_found(Message.objects.all(),id=kwargs.get("id"))
        if message.from_user !=  request.user :
            raise PermissionDenied
        message.delete()
        return JsonResponse({"message":"Message deleted Successfully","data":[]})



class UserSocketMessageView(LogindInUserView):

    def get(self,request,*args,**kwargs):
        room_name = "hello"
        return render(request,"chat.html",{"room_name":room_name})





        

