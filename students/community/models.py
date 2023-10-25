from django.db import models
from django.contrib.auth.models import User

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default="")
    datetime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    mobile = models.CharField(max_length=100, default='')
    profession = models.CharField(max_length=100, default="")
    field = models.CharField(max_length=100, default='')
    bio = models.TextField(max_length=1000, default="Create your Community")  # Changed from TimeField to TextField
    profile = models.ImageField(null=True, default='static/download.jpeg', upload_to='static/')  # Removed the comma after upload_to

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class postUser(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    threads = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=100)
    groupMembers = models.IntegerField(default = 1)
    timeCreated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.threads}"

class Discussion(models.Model):
    thread = models.ForeignKey(postUser, on_delete=models.CASCADE)
    comments = models.TextField(max_length=100000)
    writers = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(null=True, blank=True ,upload_to='static/')
    def __str__(self):
        return f"{self.thread}"
class other(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
