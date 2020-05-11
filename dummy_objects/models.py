from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Product(models.Model):
    label = models.CharField(max_length=255)
    price = models.IntegerField()
