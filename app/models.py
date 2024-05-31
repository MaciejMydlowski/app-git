from django.conf import settings
from django.db import models
from django.utils import timezone


#class Post(models.Model):  Post -> Przegląd

class MatkiPszczele(models.Model):  #MovieGenres
    matka = models.CharField(max_length=128)
    def __str__(self):
        return self.matka
class TypUla(models.Model): #MovieActors
    typ_ula = models.CharField(max_length=64)
    def __str__(self):
        return self.typ_ula
class DodawanieUla(models.Model):   #WatchedMovies
    RATES = (
        ('8', '8 ramek'),
        ('9', '9 ramek'),
        ('10', '10 ramek'),
    )
    nazwa = models.CharField(max_length=128)    #title
    install_date = models.DateTimeField('data postawienia')
    matka_date = models.DateTimeField('data podania matki')
    matka = models.ManyToManyField(MatkiPszczele)
    typ_ula = models.ManyToManyField(TypUla)
    def publish(self):
        self.save()
    def __str__(self):
        return self.nazwa

class Przeglad(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#3

#class MovieGenres(models.Model):#gatunek filmu
#    genre = models.CharField(max_length=128)

#    def __str__(self):  #4
#        return self.genre   #4
#class MovieActors(models.Model):
 #   first_name = models.CharField(max_length=64)
 #   last_name = models.CharField(max_length=64)
 #   age = models.IntegerField(default=0)

 #   def __str__(self):  #4
 #       return self.first_name + " " + self.last_name   #4
#class WatchedMovies(models.Model):
  #  RATES = (
   #     ('1', 'Okropny'),
   #     ('2', 'Słaby'),
   #     ('3', 'Średni'),
   #     ('4', 'Dobry'),
    #    ('5', 'Znakomity'),
   # )
   # title = models.CharField(max_length=128)
   # release_date = models.DateTimeField('data premiery')
   # stars = models.ManyToManyField(MovieActors)
   # genre = models.ForeignKey(MovieGenres, on_delete=models.CASCADE)
   # rate = models.CharField(max_length=1, choices=RATES)
   # review = models.TextField(blank=True)  #7

   # def __str__(self):  #4
    #    return self.title   #4
#3
#7
#class MovieReview(models.Model):
   # review = models.TextField(blank=False)
   # first_name = models.CharField(max_length=64)
    #last_name = models.CharField(max_length=64)
    #watchedMovies = models.ForeignKey(WatchedMovies, on_delete=models.CASCADE)
    #def __str__(self):
       # return self.review
#7
