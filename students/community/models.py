from django.db import models
from django.contrib.auth.models import User

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    mobile = models.CharField(default='', max_length=100)
    profession = models.CharField(max_length=100, default="")
    field = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class postUser(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    threads = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=100)
    def __str__(self):
        return f"{self.threads}"

class Discussion(models.Model):
    thread = models.ForeignKey(postUser, on_delete=models.CASCADE)
    comments = models.TextField(max_length=100000)
    writers = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.thread}"
