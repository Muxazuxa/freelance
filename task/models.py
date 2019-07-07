from django.db import models
from user.models import UserProfile

# Create your models here.fdfg


class Task(models.Model):
    owner = models.ForeignKey(UserProfile, related_name='tasks', on_delete=models.CASCADE)
    executor = models.ForeignKey(UserProfile, related_name='executor', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{}-{}'.format(self.title, self.price)
