from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

#......
class Details(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='details/', blank=True)