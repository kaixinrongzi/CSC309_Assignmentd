from django.db import models

# Create your models here.
class Paragraph(models.Model):
    likes = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    def __str__(self):
        return f"Paragraph {self.id} ({self.likes} Likes)"