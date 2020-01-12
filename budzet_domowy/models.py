from django.db import models
from django.utils import timezone


class Platnosc(models.Model):

    typ = models.TextField() #wpływy czy wydatki
    kategoria = models.TextField() #pozyczka, rata, wyplata,
    nazwa = models.TextField() #nazwa wlasna platnosci, np. rata 2
    kwota = models.TextField() #kwota
    data_graniczna = models.DateField # data do ktorej mam wykonac platnosci
    data_platnosci = models.DateField # data wykonania platnosci
    tytul_przelewu = models.TextField # tytul przelewu np. nr faktury
    nr_konta = models.TextField # numer konta do przelewu

    def payment_date(self):
        self.data_platnosci = timezone.now()
        self.save()

    def __str__(self):
        return self.kategoria