from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    username = models.CharField(max_length = 200)
    user_profile_img = models.CharField(max_length = 300)
    post_img = models.CharField(max_length = 300)
    likes = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalPost(Posts):
    user = models.ForeignKey(User, on_delete = models.CASCADE)