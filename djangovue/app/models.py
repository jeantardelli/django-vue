from django.db import models

# Create your models here.
class Band(models.Model):
    """Table schema to store a band."""
    name = models.CharField(max_length=64)
    area = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    date_formed = models.DateTimeField()

    def __repr__(self):
        return '<Name %s>' % self.name

class Album(models.Model):
    """Table schema to store albumns."""
    name = models.CharField(max_length=64)
    author = models.ForeignKey('app.Band', on_delete=models.CASCADE)
    label = models.CharField(max_length=64)
    release = models.DateTimeField()

    def __repr__(self):
        return '<Name %s>' % self.name
