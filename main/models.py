from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    cooking_time = models.IntegerField()
    cooking_descr = models.TextField()
    origin_country = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    history = models.TextField(default=None)
    image = models.ImageField()

    def __str__(self):
        return self.name


