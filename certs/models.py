from django.db import models
from .config import *

# Create your models here.

class Certificate(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100)
    cert_number = models.CharField(max_length=25, unique=True)
    cert_created = models.DateTimeField(auto_now_add=True)
    gdrive_id = models.CharField(max_length=50, null=True, blank=True, default="1O0EVKgJOKO_Y4MYlz_eKuufdbcSKFsO7")

    def __str__(self):
        val = self.student_name + ", Certificate Id = " + self.cert_number
        return val
    
    def save(self, *args, **kwargs):
        val = self.cert_number
        self.slug = generate_slug(val)
        super(Certificate, self).save(*args, **kwargs)