from django.db import models
from utils.model_status import Gender,Status
from utils.models import TimeStampAbstractModel

# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractUser

class CustomUserModel(BaseUserManager):

    '''
        CREATING CUSTOM USER
    '''

    def create_user(self,email,password=None,**extra_fields):
        '''
            Create Normal Users
        '''
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        '''
            Create Super User
        '''
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True ")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        '''
            Super must have all properties of normal user
        '''
        return self.create_user(email,password,**extra_fields)
    

class User(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    username = None
    REQUIRED_FIELDS=[]
    objects=CustomUserModel()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10,choices=Gender.choices)
    date_of_birth = models.DateField(blank=True,null=True)
    profile_picture = models.ImageField("user",blank=True,null=True)
    about = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        verbose_name='User'
        verbose_name_plural="Users"

    def save(self,*args,**kwargs):
        if len(self.first_name)>0  and len(self.middle_name)>0 and len(self.last_name)>0:
            self.name =  self.first_name +" "+ self.middle_name +" "+self.last_name
        elif len(self.first_name)>0  and len(self.last_name)>0:
            self.name= self.first_name +" "+self.last_name
        super(User,self).save(*args,**kwargs)

    def __str__(self):
        return self.email
        
    

class FriendRequest(TimeStampAbstractModel):
    from_user = models.ManyToManyField(User,related_name="friend_request_sender")
    to_user = models.ManyToManyField(User,related_name="friend_request_receiver")
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)

    def __str__(self):
        return str(self.id)+ " " +str(self.from_user.all().first().name) +"sends friend requset to "+ str(self.to_user.all().first().name)
    

