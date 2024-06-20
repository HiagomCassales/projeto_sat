from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('admin', 'Admin'),
        ('sgdc', 'SGDC'),
        ('lessonia', 'Lessonia'),
        ('infraestrutura_critica', 'Infraestruturas Críticas'),
        ('clima_espacial', 'Clima Espacial'),
        ('contratos_imagens', 'Contratos de Imagens'),  # Nova categoria adicionada aqui
    )
    name = models.CharField(max_length=25, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()


class User(AbstractUser):
    categories = models.ManyToManyField(Category, blank=True)
    is_approved = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
