from django.db import models
from utils.models import TimeStampAbstractModel
from usermanagement.models import User
from utils.model_status import LikeChoices
from django.db.models import Q
# Create your models here.



class Post(TimeStampAbstractModel):
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_post")

    def __str__(self):
        return str(self.description)
    
    @property
    def get_likes(self):
        likes = Like.objects.filter(Q(post=self) & Q(is_liked=True))
        return len(likes)


class Like(TimeStampAbstractModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_likes")
    reaction = models.CharField(max_length=10,choices=LikeChoices.choices,default=LikeChoices.LIKE)
    liked_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="liked_user")
    is_liked = models.BooleanField(default=False)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=["post","liked_user"],name="unique_like")
        ]

    def __str__(self):
        return  str(self.liked_user.id)
    


class Comment(TimeStampAbstractModel):
    message = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment_user")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment_post")

    def __str__(self):
        return str(self.message)


class PostImages(TimeStampAbstractModel):
    image = models.ImageField(upload_to="media/",blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_image_post")

    def __str__(self):
        return str(self.post.id)
    


class SharedPost(TimeStampAbstractModel):
    user = models.ManyToManyField(User,related_name="user_sharer_post")
    post = models.ManyToManyField(Post,related_name="post_sharer_post")
    
