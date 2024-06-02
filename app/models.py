from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms

class MatkiPszczele(models.Model):  
    matka = models.CharField(max_length=128)
    def publish(self):
        self.save()
    def __str__(self):
        return self.matka

class TypUla(models.Model): 
    typ_ula = models.CharField(max_length=20)
    def publish(self):
        self.save()
    def __str__(self):
        return self.typ_ula

class Lokalizacja(models.Model): 
    miejsce = models.CharField(max_length=20)
    def publish(self):
        self.save()
    def __str__(self):
        return self.miejsce

class PosiadaneUle(models.Model):
    RATES = (
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    miejsce = models.ManyToManyField(Lokalizacja)
    nazwa = models.CharField(max_length=15)  
    install_date = models.DateField('data postawienia')
    matka_date = models.DateField('data podania matki')
    matka = models.ManyToManyField(MatkiPszczele)
    typ_ula = models.ManyToManyField(TypUla)
#    ilosc_ramek = models.DecimalField( max_digits=15, decimal_places=0)
    ilosc_ramek = models.CharField(max_length=2, choices=RATES)
    aktywny = models.BooleanField()
    #aktywny = models.CharField(max_length=1, choices=RATES)
    def publish(self):
        self.save()
    def __str__(self):
        return self.nazwa
