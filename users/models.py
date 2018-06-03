from django.db import models


# === Modele:  ===
class UserProfile(models.Model):
    """
    Model stworzony, by w razie potrzeby móc przechowywać dodatkowe informacje 
    o użytkowniku - niezwiązane z autentykacją.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


