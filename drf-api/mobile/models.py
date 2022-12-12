from django.db import models


from django.contrib.auth import get_user_model
# Create your models here.

class Mobile(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    mobile_type=models.CharField(max_length=255)
    img_url=models.TextField(default='no img')
    description=models.TextField(blank=True)
    price= models.IntegerField()
    def __str__(self):
        return self.mobile_type