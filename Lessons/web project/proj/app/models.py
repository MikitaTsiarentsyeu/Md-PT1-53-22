from distutils.command.upload import upload
from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=500, blank=False)
    email = models.EmailField(blank=False, primary_key=True)

class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('p', 'public')]

    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to="uplods")
    issued = models.DateTimeField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)