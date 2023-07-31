from django.contrib import admin
from .models import user_profile , post_details , likePost , follower
# Register your models here.
admin.site.register(user_profile)
admin.site.register(post_details)
admin.site.register(likePost)
admin.site.register(follower)