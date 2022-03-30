from django.db import models

# Create your models here.
class NbaNews(models.Model):
    url = models.URLField(default='', max_length=200, unique=True)
    title = models.CharField(default='', max_length=40)
    imgsrc = models.URLField(default='', max_length=200)
    creator = models.CharField(default='', max_length=40)
    post_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title