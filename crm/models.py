from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    options=(
        ('male','male'),
        ('female','female')
    )
    gender=models.CharField(max_length=100,choices=options,default='male')
    salary=models.PositiveIntegerField()
    email=models.EmailField()
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    address=models.CharField(max_length=150)

    def __str__(self) -> str:
        self.name



