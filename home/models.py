from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    experience = models.TextField()

    def __str__(self):
        return self.name
