from django.db import models

# Create your models here.
class Post(models.Model):
    #title
    title = models.CharField(max_length=100)
    #body
    # body = models.CharField(max_length=2000)
    body = models.TextField(blank=True)
    #featured image
    image = models.ImageField(upload_to='images/')

    # this is displayed on admin area
    def __str__(self):
        return self.title

