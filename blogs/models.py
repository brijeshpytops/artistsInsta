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

class ArtistProfile(BaseClass):
    artist = models.OneToOneField(
        Artist,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    profile = models.ImageField(
        upload_to='Artist-profiles/',
        null=False,
        blank=False,
    )
    bio = models.TextField(
        null=False,
        blank=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    twiiter = models.URLField(
        null=True,
        blank=True,
    )
    facebook = models.URLField(
        null=True,
        blank=True,
    )
    instagram = models.URLField(
        null=True,
        blank=True,
    )
    

    
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


class Photography(BaseClass):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='photographies',
    )
    photo_img = models.ImageField(
        upload_to='photographies/',
        null=False,
        blank=False,
    )
    photo_tag = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

class Contacts(BaseClass):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='contacts',
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False,
    )
    subject = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    message = models.TextField(
        null=False,
        blank=False,
    )


    

        
