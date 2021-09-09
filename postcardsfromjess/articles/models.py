from django.db import models
from django.db.models.fields import DateField, SlugField

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # add in author later

    # defines how an article is going to look in admin section and shell
    def __str__(self):
        return self.title

    # method to show only a snippet of the article on articles page
    def Snippet(self):
        return self.body[:50] + '...'