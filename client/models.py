from django.db import models
import datetime
import os
def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
# Create your models here.
class user_info(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)  
    phone_number = models.CharField(max_length=10,null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=False, blank=False)

    def __str__(self):
        return self.name