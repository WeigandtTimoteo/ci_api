from django.db import models

class Property(models.Model):
    STAGE_CHOICES = [
        ('CONSTRUCTION', 'En construcción'),
        ('NEW', 'A estrenar'),
        ('USED', 'Años de antigüedad'),
    ]

    OPERATION_CHOICES = [
        ('SALE', 'Venta'),
        ('RENT', 'Alquiler'),
    ]

    title = models.CharField(max_length=255, default="")
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES, default='SALE')
    description = models.TextField()
    total_area = models.DecimalField(max_digits=10, decimal_places=2)
    covered_area = models.DecimalField(max_digits=10, decimal_places=2)
    age_status = models.CharField(max_length=20, choices=STAGE_CHOICES)
    age_years = models.PositiveIntegerField(default=0)
    rooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    toilettes = models.PositiveIntegerField(default=0)
    garages = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_operation_type_display()}) - {self.location}"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return f"Foto de {self.property.title}"