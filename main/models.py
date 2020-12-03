from django.db import models
from django.utils import timezone
from django.conf import settings 
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)   
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


