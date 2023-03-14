from django.db import models

# Create your models here.
class Canhoto(models.Model):
    codigo = models.IntegerField(default=False)
    data = models.DateField()
    situacao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ('codigo',)

    def __str__(self):
        return self.canhoto