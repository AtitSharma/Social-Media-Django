from usermanagement.models import FriendRequest
from utils.utility import get_or_not_found
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class IsRealFriendRequestAccepterUser(AccessMixin):
    def dispatch(self,request,*args,**kwargs):
        query = get_or_not_found(FriendRequest.objects.all(),id=kwargs.get("id"))
        if query.to_user.all().first() != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    