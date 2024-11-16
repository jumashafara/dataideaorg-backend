from django.db import models

# Create your models here.
# resource class
class Resource(models.Model):
    name = models.CharField(max_length=100, default='New Resource')
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='library/', blank=True)
    def __str__(self):
        return self.name
