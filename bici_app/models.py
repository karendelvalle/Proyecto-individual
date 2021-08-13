from django.db import models
from django.db.models.deletion import CASCADE
import re
import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'El nombre debe tener al menos 2 caracteres'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'El apellido debe tener al menos 2 caracteres'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['register_email']):    
            errors['register_email'] = "La dirección de correo electrónico debe ser válida."
        if len(postData['register_password']) < 8:
            errors['register_password'] = 'El password debe tener al menos 8 caracteres'
        if postData['register_password'] != postData['confirm']:
            errors['register_password'] = "La contraseña debe ser la misma"
        return errors
    def login_validator(self, postData):
        errors ={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):    
            errors['login_email'] = "La dirección de correo electrónico debe ser válida."
        if len(postData['login_password']) < 8:
            errors['login_password'] = 'El password debe tener al menos 8 caracteres'
        return errors     

class EventoManager(models.Manager):       
    def evento_validator(self, postData):
        errors ={}
        if len(postData['nombre']) < 2:
            errors['nombre'] = 'El nombre debe tener 2 o más caracteres.'
        if len(postData['encuentro']) < 5:
            errors['encuentro'] = 'El encuentro debe tener 5 o más caracteres'
        if len(postData['termino']) < 5:
            errors['termino'] = 'El termino debe tener 5 o más caracteres'
        if len(postData['ruta']) < 5:
            errors['ruta'] = 'La ruta debe tener 5 o más caracteres'
        return errors
    
class MessageManager(models.Manager):
    def mensaje_validator(self, postData):
        errors ={}
        if len(postData['mensaje']) < 2:
            errors['mensaje'] = 'El mensaje debe tener 2 o más caracteres.'
        return errors
class ComentarioManager(models.Manager):
    def comentario_validator(self, postData):
        errors ={}
        if len(postData['comentar_mensaje']) < 2:
            errors['comentar_mensaje'] = 'El comentario debe tener 2 o más caracteres.'
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)  
    objects = UserManager()
    def __str__(self):
        return f"<{self.first_name} {self.last_name} {self.email} {self.id}>"

class Evento(models.Model):
    nombre=models.CharField(max_length=45, null=True)
    creador=models.ForeignKey(User, related_name="user_creador", on_delete=CASCADE)
    encuentro=models.TextField(null=True)
    termino=models.TextField(null=True)
    ruta=models.TextField(null=True)
    fecha=models.DateField(null=True, blank=True)
    hora=models.TimeField(null=True, blank=True)
    dificultad=models.IntegerField(null=True)
    users_add_evento=models.ManyToManyField(User, related_name="user_eventos")
    objects = EventoManager()
    def __str__(self):
        return f"<{self.creador} {self.ruta} {self.fecha} {self.id}>"

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=CASCADE)
    evento = models.ForeignKey(Evento, related_name= "users_message", on_delete= CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager() 

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="user_comments", on_delete=CASCADE)
    message = models.ForeignKey(Message, related_name="message_comments", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ComentarioManager()
    def __str__(self):
        return f"{self.comment}"