from django.db import models

# Create your models here.
class Blogpost(models.Model):
    PosttId = models.AutoField(primary_key=True)
    MainHeading = models.CharField(max_length=500)
    MainDes = models.CharField(max_length=10000)
    SubHeading1 = models.CharField(max_length=100,default = '')
    SubDes1 = models.CharField(max_length=500, default = '')
    SubHeading2 = models.CharField(max_length=100, default = '')
    SubDes2 = models.CharField(max_length=500, default = '')
    PostDate = models.DateField(auto_now_add=True)
    image= models.ImageField(upload_to="blog",default="")

    def __str__(self):
        return self.MainHeading[0:50]
    
