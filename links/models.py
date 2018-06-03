from django.db import models
from django.utils import timezone


# === Modele:  ===


class Link(models.Model):
    """
    Model reprezentujący klasę link. Oprócz standardowych atrybutów 
    wskazujących na pole w bazie danych, istnieje również pole autor wskazujace 
    na obiekt klasy UserProfile.
    """
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(
        'users.UserProfile', on_delete=models.DO_NOTHING)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model reprezentujący klasę komentarz. Pole link wskazuje na obiekt klasy 
    Link, do którego odnosi się komentarz. Podobnie w przypadku autora. Pole 
    parent_comment wskazuje natomiast na obiekt klasy Comment - wykorzystujemy 
    to przy tworzeniu drzewiastej struktury komentarzy.
    """
    link = models.ForeignKey('Link', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(
        'users.UserProfile', on_delete=models.DO_NOTHING)
    published_date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    """
    Model Like został stworzony, aby móc ograniczyć liczbę "polubień" postu lub 
    komentarza dla danego użytkownika. Tworzone sa pary użytkownik-link lub 
    użytkownik-komentarz.
    """
    link = models.ForeignKey('Link', on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
