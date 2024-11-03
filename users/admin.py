from django.contrib import admin

from users.models import Passport, Citizen, UserProfile, Post

admin.site.register(Passport)
admin.site.register(Citizen)
admin.site.register(UserProfile)
admin.site.register(Post)

