from django.conf import settings
from django.db import models


class Note(models.Model):
    note_text = models.CharField(max_length=500)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='note_id')

    note_create_date = models.DateTimeField(auto_now_add=True)
    note_notify_start = models.DateTimeField(null=True, blank=True)
    note_notify_gap = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"Заметка от {self.note_create_date.strftime("%Y-%m-%d %H:%M")} гласит:\n {self.note_text}"
