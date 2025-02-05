from django.db import models

import uuid

# Create your models here.
class BaseClass(models.Model):
    art_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True

class Artist(BaseClass):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    mobile = models.CharField(
        max_length=15,
        unique=True,
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    otp = models.CharField(default='1111', max_length=6)

    
class Post(BaseClass):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    post_img = models.ImageField(
        upload_to='posts/',
        null=False,
        blank=False,
    )
    post_tag = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    post_title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    content = models.TextField(
        null=False,
        blank=False,
    )

    

        
