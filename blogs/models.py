from django.db import models
from tinymce.models import HTMLField 

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60, default="TITLE")
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default="anurag")
    description = models.CharField(max_length=100, default="wot???")
    thumbnail = models.ImageField(blank=True, upload_to='static')
    text_area = HTMLField()


    def yearpublished(self):
        return self.date.strftime('%b %d, %Y')

    def __str__(self):
        return self.title
