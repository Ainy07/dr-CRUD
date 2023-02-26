from django.db import models


CATEGORY_CHOICE = (
    ('C', 'Cardiologists'),
    ('N', 'neurologists'),
    ('S', 'surgeons'),
    ('G', 'gynecologists'),
    ('E', 'endocrinologists'),
    ('D', 'dentists')
)
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=400)
    image = models.ImageField(upload_to='Doctor/')
    category = models.CharField(choices=CATEGORY_CHOICE , max_length=200)