from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_diplay = ["title", "subtitle", "body", "created_on"]

admin.site.register(Post, PostAdmin)

