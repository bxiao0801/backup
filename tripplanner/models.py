from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#User includes username,password,email,first_name,last_name
#Addtional includes additional information, i.e registration info-User info
class AddManager(models.Manager):
    def create_add(self,user,phone,location,city,country,zip,con_password,dob,gender):
        add=self.create(user=user,phone=phone,location=location,city=city,country=country,zip=zip,\
                        con_password=con_password,dob=dob,gender=gender)
        return add

class AddSearch(models.Manager):
    def create_sea(self,user,city,bar,coffee,restaurant,food,art,fashion,film,holiday,music,shopping,sport,\
                   outdoor,acti,trend):
        sea=self.create(user=user,city=city,bar=bar,coffee=coffee,restaurant=restaurant,food=food,art=art,\
                        fashion=fashion,film=film,holiday=holiday,music=music,shopping=shopping,sport=sport,\
                        outdoor=outdoor,acti=acti,trend=trend)
        return sea

class Additional(models.Model):
    user=models.OneToOneField(User,primary_key=True)
    phone=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    con_password=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

    objects=AddManager()


class Search(models.Model):
    user=models.ForeignKey(User)
    city=models.CharField(max_length=100)
    bar=models.BooleanField(default=False)
    coffee=models.BooleanField(default=False)
    restaurant=models.BooleanField(default=False)
    food=models.CharField(max_length=100)

    art=models.BooleanField(default=False)
    fashion=models.BooleanField(default=False)
    film=models.BooleanField(default=False)
    holiday=models.BooleanField(default=False)
    music=models.BooleanField(default=False)
    shopping=models.BooleanField(default=False)
    sport=models.BooleanField(default=False)
    outdoor=models.BooleanField(default=False)
    acti=models.CharField(max_length=100)

    trend=models.BooleanField(default=False)

    objects=AddSearch()