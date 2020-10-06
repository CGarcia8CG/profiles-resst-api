from django.contrib import admin
#agregar este import de la API
from profiles_api import models

# Register your models here.
#Para accesar al sitio de administradores, lo habilita
admin.site.register(models.UserProfile)
#Para testear
#6 python manage.py runserver 0.0.0.0:8000 --> http://127.0.0.1:8000/ en el navegador ---> http://127.0.0.1:8000/admin
#7 en el navegador, Auth Token lo permite el REST framework y permite ser una API
#7 User profiles viene de lo que se escribio (UserProfile)
#7 Groups viene de Django base
