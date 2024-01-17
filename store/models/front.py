from django.db import models
class Front(models.Model):
    image = models.ImageField(upload_to='uploads/products/',null=True)

    @staticmethod
    def get_all_gallery_img():
        return Front.objects.all()
