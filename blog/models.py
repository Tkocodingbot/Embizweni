from django.db import models

class Blog(models.Model):
    tittle = models.CharField(max_length=150)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.tittle
