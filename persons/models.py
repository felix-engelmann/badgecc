from django.db import models

# Create your models here.

class Right(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.name)

class Role(models.Model):

    name = models.CharField(max_length=50)
    rights = models.ManyToManyField(Right, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Department(models.Model):

    name = models.CharField(max_length=50)
    background = models.ImageField()
    rights = models.ManyToManyField(Right, null=True, blank=True)
    default_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Person(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    department = models.ForeignKey(Department)
    role = models.ForeignKey(Role, null=True, blank=True)
    printed = models.BooleanField(default=False)
    extra_rights = models.ManyToManyField(Right, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.name)