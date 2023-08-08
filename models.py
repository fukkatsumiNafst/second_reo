from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
import datetime

class Adv(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    prise = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='отметьте если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:green; font-weight: bold"></span>',
                created_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    class Meta:
        db_table = 'advertisements'

    def __str__(self) -> str:
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"