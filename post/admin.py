from django.contrib import admin
from post.models import Post,Like,Comment,PostImages,SharedPost

# Register your models here.

admin.site.register(PostImages)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(SharedPost)

