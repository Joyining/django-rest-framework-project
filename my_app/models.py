from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=1000, default='')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
