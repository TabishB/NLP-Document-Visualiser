from django.db import models
from visualiser.validators import validate_file_extension
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
import os
import re

# Create your models here.
class FileDoc(models.Model):

    topics = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(20)], blank=True, null=True)
    document = models.FileField(upload_to='visualiser/management/commands/documents/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 255, default='error', blank=True, null=True)

    def __str__(self):
        return self.document

    def file(self):
        return os.path.basename(self.document.name)

    def filename(self):
        s = os.path.basename(self.document.name)
        file = s[:s.find(".")]
        return file



class WordTestTabish(models.Model):

    word = models.CharField(max_length=255)
    frequency = models.IntegerField()


# ## NEW MODEL
# class Word(models.Model):
#     #Attrbutes in the models
#     word = models.CharField(max_length=255)
#     frequency = models.IntegerField()
