from django.db import models


class Project(models.Model):
    titel = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="portfol/images")
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):
        return u"{}".format(self.titel)