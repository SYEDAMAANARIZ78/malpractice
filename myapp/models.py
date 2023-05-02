from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Malpracticentry(models.Model):
    studentname = models.CharField(max_length=50)
    registrationnumber = models.CharField(max_length=50)
    facultyadvisor = models.CharField(max_length=50)
    facultyademail = models.EmailField(max_length=50)
    squadname = models.CharField(max_length=50)
    enquirydate = models.DateField(null=True,blank=True)
    squademail = models.EmailField(max_length=50)
    malpracticedetail = models.CharField(max_length=50)
    examination = models.CharField(max_length=50)
    subjectcode = models.CharField(max_length=50)
    subjectname = models.CharField(max_length=50)
    actiontaken = models.CharField(max_length=50, blank=True)
    
    # ...
    # def get_absolute_url(self):
    #     return reverse('malform', args=[self.slug])

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.studentname
    
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username