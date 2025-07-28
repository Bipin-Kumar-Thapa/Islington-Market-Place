from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):  #without models it will understand it as a normal class and it will not create a table.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name #instead of objects it will show name of the category


class blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    

