from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    package_type=models.CharField(max_length=100)
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.name
