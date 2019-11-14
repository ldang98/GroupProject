from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Link(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()
    links=models.ManyToManyField(Category)

    def __str__(self):
        return self.title


