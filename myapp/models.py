from django.db import models
import random

# Create your models here.
class PunktVidachi(models.Model):
    nazvanie = models.CharField(max_length=300)

class Postavshik(models.Model):
    nazvanie = models.CharField(max_length=300)

class Proizvoditel(models.Model):
    nazvanie = models.CharField(max_length=300)

class Tovar(models.Model):
    nazvanie = models.CharField(max_length=300, verbose_name="Название")
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    skidka = models.IntegerField(default=0)
    foto = models.ImageField(upload_to="photos/", blank=True)
    opisanie = models.CharField(max_length=300, verbose_name="Описание")
    articul = models.CharField(max_length=300, verbose_name="Название", unique=True)
    edinizaIzmerenia = models.CharField(max_length=300, verbose_name="Единица измерения")
    kategoriya = models.CharField(max_length=300, verbose_name="Категория")
    proizvoditel = models.ForeignKey(Proizvoditel)
    postavshik = models.ForeignKey(Postavshik)

    @property
    def cena_so_skidkoi(self):
        return self.cena * (1 - self.skidka / 100)
    
    class Meta: 
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

def poluchit_sluchaini_cod():
    return random.randint(100, 999)

class Zakaz(models.Model):
    STATUSES = [{"new": "Новый"}, {"done": "Завершен"}]
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    klient = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    dataDostavki = models.DateField()
    dataZakaza = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUSES, default="new")
    cod_poluchenia = models.IntegerField(max_digits=3, default=poluchit_sluchaini_cod())
    punktVidachi = models.ForeignKey(PunktVidachi)


     