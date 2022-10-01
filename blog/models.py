from django.db import models


class Blog(models.Model):
    titel = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=250)
    text = models.TextField()
    photo = models.ImageField(upload_to="blog/images", blank=True)

    def __str__(self):
        return u"{}".format(self.titel)
# Create your models here.
