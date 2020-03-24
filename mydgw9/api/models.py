from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
    return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count
    }