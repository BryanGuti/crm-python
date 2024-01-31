from django.db import models


class Record(models.Model):
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
