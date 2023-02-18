from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Good')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name='Published date')

class Meta:
    verbose_name_plural = 'Announcement'
    verbose_name = 'Announcement'
    ordering = ['-published']

