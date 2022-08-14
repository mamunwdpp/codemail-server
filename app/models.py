from django.db import models

class User(models.Model):
    name = models.CharField(max_length=11, unique=True, blank=False, null=False)
    password = models.CharField(max_length=11, unique=False, blank=False, null=False)
    mac = models.CharField(max_length=40, unique=False, blank=False, null=False, default=0, verbose_name="UUID")
    active = models.BooleanField(default=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    