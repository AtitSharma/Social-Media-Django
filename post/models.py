from django.db import models
from utils.models import TimeStampAbstractModel
from usermanagement.models import User
from utils.model_status import LikeChoices,PostStatus
from django.db.models import Q
from django.core.exceptions import PermissionDenied



class Post(TimeStampAbstractModel):
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_post")
    status = models.CharField(max_length=10,choices=PostStatus.choices,default=PostStatus.PUBLIC)

    def __str__(self):
        return str(self.id) + " "+ str(self.description) 
    
    @property
    def get_likes(self):
        likes = Like.objects.filter(Q(post=self) & Q(is_liked=True))
        return len(likes)
    
    @property
    def get_comments(self):
        comments = Comment.objects.filter(post=self)
        return len(comments)
    
    @property
    def shared_post_count(self):
        shared_count = SharedPost.objects.filter(post=self).all()
        return len(shared_count)
    
    def get_is_liked_by_user(self,request):
        like = Like.objects.filter(liked_user=request.user,post=self,is_liked=True).first()
        return True if like else False




class Like(TimeStampAbstractModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_likes",blank=True,null=True)
    reaction = models.CharField(max_length=10,choices=LikeChoices.choices,default=LikeChoices.LIKE)
    liked_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="liked_user")
    is_liked = models.BooleanField(default=False)
    shared_post = models.ForeignKey('SharedPost',on_delete=models.CASCADE,related_name="shared_post_likes",blank=True,null=True)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=["post","liked_user"],name="unique_like"),
            models.UniqueConstraint(fields=["shared_post","liked_user"],name="unique_shared_post_like"),
        ]

    def __str__(self):
        return  str(self.liked_user.id)
    
    def save(self,*args,**kwargs):
        if not self.is_post_or_is_liked():
            raise PermissionDenied
        super(Like,self).save(*args,**kwargs)

    
    def is_post_or_is_liked(self):
        if (self.post and self.shared_post) or (not self.post and not self.shared_post):
            return False
        return True


class Comment(TimeStampAbstractModel):
    message = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment_user")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment_post",blank=True,null=True)
    shared_post = models.ForeignKey('SharedPost',on_delete=models.CASCADE,related_name="comment_shared_post",blank=True,null=True)

    def __str__(self):
        return f"{self.id}   {self.message}"
    

    def save(self,*args,**kwargs):
        if not self.is_post_or_is_shared_post():
            raise PermissionDenied
        super(Comment,self).save(*args,**kwargs)

    
    def is_post_or_is_shared_post(self):
        if (self.post and self.shared_post) or (not self.post and not self.shared_post):
            return False
        return True


class PostImages(TimeStampAbstractModel):
    image = models.ImageField(upload_to="posts",blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_image_post")

    def __str__(self):
        return str(self.post.id)
    


class SharedPost(TimeStampAbstractModel):
    description = models.CharField(max_length=255,blank=True,null=True)
    user = models.ManyToManyField(User,related_name="user_sharer_post")
    post = models.ManyToManyField(Post,related_name="post_sharer_post")

    @property
    def get_likes(self):
        likes = Like.objects.filter(Q(shared_post=self) & Q(is_liked=True))
        return len(likes)
    
