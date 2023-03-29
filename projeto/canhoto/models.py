from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Canhoto(models.Model):
    codigo = models.IntegerField('código',default=False, unique=True)
    data = models.DateField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.CharField(max_length=100, default='')
    conferencia = models.BooleanField('conferência', default=False)

    class Meta:
        ordering = ('codigo',)

    def __str__(self):
        return f'{self.codigo}'
    
    def get_absolute_url(self):
        return reverse_lazy('canhoto:canhoto_detail', kwargs={'pk':self.pk})
    
class Movies(models.Model):
   file = models.FileField(upload_to='scanning_pdfs/')