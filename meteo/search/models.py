from django.db import models

from weather.models import CityCached


class SearchHistory(models.Model):
    session_key = models.CharField(max_length=124, help_text="Сессия пользователя",)
    city = models.ForeignKey(CityCached, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Поиск: {self.city.name} ({self.session_key})"


class SearchStat(models.Model):
    city = models.OneToOneField(
        CityCached,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Статистика для {self.city.name}: {self.count}"
