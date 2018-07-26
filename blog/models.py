## CREATING BLOG POST MODELS
# WARNING: after creating a model, create tables for that model in database by: makingmigrations & migrate
# Imports
from django.db import models
from django.utils import timezone


# models
class Post(models.Model):
    """
    docstring for Post.
    models.Model means that the Post is a Django Model, Django knows that it
    should be saved in the database.
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # Link to another model
    title = models.CharField(max_length = 200) # CharField for limited text
    text = models.TextField() # TextField for unlimited text
    created_date = models.DateTimeField(default=timezone.now) # DateTimeField for date and time
    publised_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publised_date = timezone.now()
        self.save()

    def __str__(self):
        """returns this if str is expected as output."""
        return self.title
