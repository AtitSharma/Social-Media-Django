from django.contrib.auth.mixins import AccessMixin,LoginRequiredMixin
from django.views import View




class LogindInUserView(LoginRequiredMixin,View):
    pass
