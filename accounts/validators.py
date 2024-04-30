import os
from django.core.exceptions import ValidationError
from django import forms

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        print('___________________________________true')
        raise ValidationError('Unsupported file extension.')
    else :
        print('___________________________________false')