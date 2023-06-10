from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


JOB_TYPE = (
    ('P', 'Part Time'),
    ('F', 'Full Time'),
)



class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)



class Apply(models.Model):
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    cv = models.FileField(upload_to='CV')
    cover_letter = models.TextField()
    website = models.URLField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    city = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email