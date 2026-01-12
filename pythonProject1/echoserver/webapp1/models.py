from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    Author = models.CharField(max_length=200, null=True)
    Price = models.IntegerField()

    def __str__(self):
        return str(self.title)


class User(AbstractUser):
    first_name = models.CharField('Имя', max_length=200)
    email = models.EmailField('Email', unique=True)
    ROLES = (
        ('regular user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='regular user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.username

    def is_admin(self):
        return self.role == 'admin'