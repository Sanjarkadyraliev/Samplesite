from django.db import models

class Goods(models.Model):
    title = models.CharField(max_length=50, verbose_name='Good')
    category = models.TextField(null=True, blank=False, verbose_name='Category')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name='Published date')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

class Meta:
    verbose_name_plural = 'Announcement'
    verbose_name = 'Announcement'
    ordering = ['-published']





class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    def __str__(self):
        return self.name



class Meta:
    verbose_name_plural = "Рубрики"
    verbose_name = 'Рубрика'
    ordering = ['name']




