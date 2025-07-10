from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            unique_together = ('user', 'name')

    def __str__(self):
          return f"{self.name} ({self.user.username})"
