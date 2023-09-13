from django.db import models

from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from datetime import date


class Department(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}-{self.address}'
class Positions(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    birth_date = models.DateField()
    # salary = models.FloatField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Используем DecimalField для зарплаты
    receipt_date = models.DateField(default=timezone.now() + timezone.timedelta(days=1))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fullname}-{self.birth_date}-{self.salary}-{self.receipt_date}-{self.department}-{self.position}'