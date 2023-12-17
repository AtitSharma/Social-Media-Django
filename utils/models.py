from django.db import models
# Create your models here.

class TimeStampAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



class OTP(TimeStampAbstractModel):
    otp = models.IntegerField()
    user = models.ForeignKey("usermanagement.User",on_delete=models.CASCADE,related_name="otp_user")