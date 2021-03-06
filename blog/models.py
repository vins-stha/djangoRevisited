from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtext = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField(auto_now=True)


def __str__(self):
    """String for representing the Model object."""
    return self.name
def __get_latest_by(date):
    return Post.objects.latest(date)