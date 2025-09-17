from django.db import models
from django.contrib.auth.models import User

class Floare(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.TextField()
    pret = models.DecimalField(max_digits=6, decimal_places=2)
    imagine = models.ImageField(upload_to='flori/', blank=True, null=True)
    stoc = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nume

# 🔴 Această clasă era greșit indentată!
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Floare, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.flower.nume}"