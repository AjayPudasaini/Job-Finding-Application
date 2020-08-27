import os
from django.core.exceptions import ValidationError

def validate_cv_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file! Please upload only .pdf, .doc, .docx')

def Validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]
    Valid_extension = ['.png', '.jpg', '.jpeg', '.gif',]
    if not ext.lower() in Valid_extension:
        raise ValidationError('Unsupported Image! only supports .png, .jpg, .jpeg, .gif')