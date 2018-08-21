from django.db import models

# Create your models here.

    
ALLERGENS = (
    ("cow's milk", "Cow's milk"),
    ('lactose', 'lactose'),
    )

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=400, default="Enter description")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images', default='generic_product.png')
    weeks_ripened = models.DecimalField(max_digits=3, decimal_places=0)

    
    def __str__(self):
        return self.name