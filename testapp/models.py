from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    auth = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.__dict__}'

    class Meta:
        db_table = 'book'


class Author(models.Model):
    name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'
