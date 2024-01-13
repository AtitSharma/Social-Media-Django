from django.shortcuts import render
from django.http import JsonResponse
from utils.permissions import LogindInUserView
from utils.utility import get_or_not_found
from message.models import Message
from usermanagement.models import User
from message.query import MessageQuery
from django.db.models import Q


class ListAllMessagesView(LogindInUserView):
    def get(self,request,*args,**kwargs):
        to_user = get_or_not_found(User.objects.all(),id=kwargs.get("id"))
        messages = Message.objects.filter(Q(Q(from_user=request.user) & Q(to_user=to_user)) | Q(Q(from_user=to_user) & Q(to_user=request.user))).order_by("created_at")
        query = MessageQuery(messages)
        return JsonResponse({"message":"All Chat History Retreved Successfully","data":query.get_all_data()})
        