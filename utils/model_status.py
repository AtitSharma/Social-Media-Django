from django.db import models



class Gender(models.TextChoices):
    MALE = '1'
    FEMALE = '2'
    OTHERS = '3'


class LikeChoices(models.TextChoices):
    HAHA = '1'
    LOVE = '2'
    WOW = '3'
    LIKE = '4'
    SAD = '5'
    ANGRY = '7'



class Status(models.TextChoices):
    
    PENDING = '1'
    ACCEPTED = '2'
    REJECTED = '3'