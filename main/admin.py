from django.contrib import admin
from .models import * ## or post (. means from same directory)
# Register your models here.
admin.site.register(Post)
admin.site.register(Author)