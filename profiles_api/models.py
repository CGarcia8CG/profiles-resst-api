from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email adress! :3')

        else:
            #Pone en minuscula
            email=self.normalize_email(email)
            user= self.model(email=email,name=name)
            #Password encriptado, no en texto---> Se vera hasheado
            user.set_password(password)
            #Guardar usuario #base de datos estandar
            user.save(using=self._db)

            return (user)

    def create_superuser(self,email,name,password):
        """Create new super user"""
        # Reusar la funcion create_user
        user= self.create_user(email,name,password)

        #is_superuser creado por PermissionMixin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return(user)





#Clase usuario ---> Esta es la nueva manera (en vez de la de Django) para manejar usuarios
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    #correo
    email = models.EmailField(max_length=255, unique=True)
    #Nombre
    name = models.CharField(max_length=255)
    #Esta conectado
    is_active = models.BooleanField(default=True)
    #Puede acceder al admin?
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #No esta mal, email sera id
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Return full name of user"""

        return (self.name)

    def get_short_name(self):
        """Return short name of user"""
        return (self.name)

    #Lo que se regresa
    def __str__(self):
        """Return string representation of the user"""

        return (self.email)
