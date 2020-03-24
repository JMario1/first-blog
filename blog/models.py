from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    Title = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    Author = models.CharField(max_length=200)
    Text = models.TextField()
    Create_date = models.TimeField(default = timezone.now)
    Published_date = models.TimeField(blank =True, null = True)

    def Publish(self):
        self.Published_date = timezone.now
        self.save()

    def __str__(self):
        return self.Title