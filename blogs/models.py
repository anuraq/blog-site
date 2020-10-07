from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=60, default="TITLE")
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default="Anonomous")
    text_area = models.TextField(default="random text lorem ipsum lipsum jipsum kipsum hiphum jism jism 2")

    def __str__(self):
        return self.title
