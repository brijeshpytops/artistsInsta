from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Artist, Post, Photography, Contacts, ArtistProfile
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Artist)
admin.site.register(ArtistProfile)
admin.site.register(Post)
admin.site.register(Photography)
admin.site.register(Contacts)