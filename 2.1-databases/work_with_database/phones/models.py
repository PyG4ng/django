from django.db import models


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField()
