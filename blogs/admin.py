from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Artist, Post
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Artist)
admin.site.register(Post)