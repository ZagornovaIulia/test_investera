from django.db import models
# *  id(integer, primary key)
# * [] title(string)
# * [] content(string)
# * [] created_at(datetime)
# * [] updated_at (datetime)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
