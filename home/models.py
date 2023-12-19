from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name