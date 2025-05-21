from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=40, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    
    def __str__(self):
        return self.name