# apps/users/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    CATEGORY_CHOICES = (
        ('admin', 'Admin'),
        ('sgdc', 'SGDC'),
        ('lessonia', 'Lessonia'),
        ('infraestrutura_critica', 'Infraestruturas Críticas'),
    )
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='sgdc')
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
