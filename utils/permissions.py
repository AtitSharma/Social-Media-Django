from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View




class LogindInUserView(LoginRequiredMixin,View):
    pass
