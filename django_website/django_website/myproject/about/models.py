from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/workers/')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='images/company/')


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
