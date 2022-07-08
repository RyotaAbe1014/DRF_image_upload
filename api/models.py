from django.db import models

# Create your models here.


def top_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'images/{0}/'.format(filename)

def top_file_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'files/{0}/'.format(filename)


class Profile(models.Model):
    top_image = models.ImageField(
        verbose_name="トップ画像", upload_to=top_image_upload_path, blank=True, null=True)


class File(models.Model):
    file = models.FileField(verbose_name="ファイル", upload_to=top_file_upload_path, blank=True, null=True)