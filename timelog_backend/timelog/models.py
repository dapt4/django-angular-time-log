from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CheckIn(models.Model):
    '''
        user = User.objects.get(id=1)
        CheckIn(user=user, ...)
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)  # CheckIn(date="2025-02-03")
    start = models.TimeField()  # CheckIn(start="08:45:00")
    end = models.TimeField()  # CheckIn(start="08:45:00")
