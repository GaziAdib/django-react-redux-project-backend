from django.db import models

# Create your models here.

# Our API Models 

class Project(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnail/images', null=True, blank=True)
    title = models.CharField(max_length=100,blank=False, null=False)
    category = models.CharField(max_length=50,blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    demo = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title