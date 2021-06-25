from django.db import models
from django.contrib.auth.models import AbstractUser

# si queremos sobreescribir tenemos que apoyarnos de la clase AbstractUser o AbstractBaseUser (si diferencia esta en los atributos que posee cada una)
#proxymodel un modelo que hereda de otro
#definir los nuevos atributos que queremos que un usuario posea
class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Customer(User):
    class Meta:
        proxy=True

    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()