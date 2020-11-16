from django.db import models

class Actors(models.Model):
    
    actor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

