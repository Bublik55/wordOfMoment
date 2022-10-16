from django.db import models

# Create your models here.


class Word(models.Model):
    owner_id = models.BigIntegerField(default=0)
    content = models.CharField(max_length=30, default="empty")
    count = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.content) + " : " + str(self.count)

