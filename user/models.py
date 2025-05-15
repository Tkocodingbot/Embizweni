from django.db import models
from django.contrib.auth.models import User

PROVINCE_CHOICES = (
    ('KwaZulu-Natal', 'KZN'),
    ('Limpopo', 'LP'),
    ('Mpumalanga', 'MP'),
    ('Gauteng', 'GP'),
    ('Western Cape', 'WC'),
    ('Eastern Cape', 'EC'),
    ('Northern Cape', 'NC'),
    ('Free State', 'FS'),
    ('North West', 'NW'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    mobile = models.CharField(default=0)
    province = models.CharField(choices=PROVINCE_CHOICES,max_length=100)
    postal_code = models.IntegerField()
    
    def __str__(self):
        return self.name
