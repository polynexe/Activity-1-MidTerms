import random
from django.db import models

# Create your models here.

def upload_image_path(instance, filename, ext=None):
    new_filename = random.randint(1, 10000)
    # name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "Activity_1_Midterms/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class Tweets(models.Model):
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
