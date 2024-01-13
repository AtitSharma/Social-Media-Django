from django.db import models
from usermanagement.models import User
from utils.models import TimeStampAbstractModel

# Create your models here.

class Message(TimeStampAbstractModel):
    from_user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="message_sender_user")
    to_user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="message_receiver_user")
    message = models.TextField()

    def __str__(self):
        return str(self.message)