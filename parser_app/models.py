from django.db import models

class Cinema(models.Model):
    title = models.CharField(max_length=230)
    image = models.ImageField(upload_to='')
