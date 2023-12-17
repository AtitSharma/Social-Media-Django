from django.conf import settings
from django.core.mail import send_mail
import random
from utils.models import OTP
from usermanagement.models import User
from post.models import Post,SharedPost,PostImages
FROM_USER = settings.EMAIL_HOST_USER

def send_email_to_verify_user(id):
    user = User.objects.get(id=id)
    otp = random.randint(1000,10000)
    subject = "Your Otp Message"
    message = f"Dear User {user.name},\nYour Otp is {otp} please use this otp before 5 minutes."
    send_mail(subject=subject,message=message,from_email=FROM_USER,recipient_list=[user.email])
    OTP.objects.create(otp=otp,user=user)




def format_posts_with_image(posts,post_images):
    images_dict = {}
    for image in post_images:
        if image.post_id not in images_dict:
            images_dict[image.post_id] = []
        images_dict[image.post_id].append(image.image.url)
    posts_with_images = []
    for post in posts:
        images = images_dict.get(post.id, []) 
        posts_with_images.append({
            'post': post,
            'images': images,
        })
    return posts_with_images


def format_shared_posts_with_image(shared_posts):
    images = []
    for shared_post in shared_posts:
        for post in shared_post.post.all():
            image = PostImages.objects.filter(post=post).values_list("image",flat=True)
            images.append({
                "post":post,
                "images":image
            })
    return images
                         
            

        
        

        # images_dict["shared_post"]=shared_post.post
        # images_dict["image"] = list(map(lambda x : shared_post.post.image.all()))

    # pass