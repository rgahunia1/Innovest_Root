
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from datetime import date

# Create your models here.


#user = models.OneToOneField(settings.AUTH_USER_MODEL)

class smbuser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_business = models.BooleanField(default=True)
    is_sofi = models.BooleanField(default=False)

    name = models.CharField(max_length = 50)
    dob = models.DateField()
    address = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)

    
    @property
    def age(self):
        today = date.today()
        db = self.dob
        age = today.year - db.year
        if today.month < db.month or today.month == db.month and today.day < db.day:
            age -= 1
        return age 



class doctor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=True)

    name = models.CharField(max_length = 50)
    dob = models.DateField()
    address = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)

    registration_no = models.CharField(max_length = 20)
    year_of_registration = models.DateField()
    qualification = models.CharField(max_length = 20)
    State_Medical_Council = models.CharField(max_length = 30)

    specialization = models.CharField(max_length = 30)

    rating = models.IntegerField(default=0)

# define sofi   
class sofi(models.Model):
    # sofi is a user and a sofiuser
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_patient = models.BooleanField(default=False)
    is_sofi = models.BooleanField(default=True)

    name = models.CharField(max_length = 50)
    dob = models.DateField()
    address = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)

    #registration_no = models.CharField(max_length = 20)
    #year_of_registration = models.DateField()
    qualification = models.CharField(max_length = 20)
    #State_Medical_Council = models.CharField(max_length = 30)

    #specialization = models.CharField(max_length = 30)

    #rating = models.IntegerField(default=0)
# end sofi




class businessinfo(models.Model):

    smbuser = models.ForeignKey(smbuser , null=True, on_delete=models.SET_NULL)

    businessname = models.CharField(max_length = 200)
    no_of_employee = models.IntegerField()
    description = ArrayField(models.CharField(max_length=200))
    revenue = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.CharField(max_length = 200)



class consultation(models.Model):

    smbuser = models.ForeignKey(smbuser ,null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(sofi ,null=True, on_delete=models.SET_NULL)
    businessinfo = models.OneToOneField(businessinfo, null=True, on_delete=models.SET_NULL)
    consultation_date = models.DateField()
    status = models.CharField(max_length = 20)





class rating_review(models.Model):

    smbuser = models.ForeignKey(smbuser ,null=True, on_delete=models.SET_NULL)
    sofi = models.ForeignKey(sofi ,null=True, on_delete=models.SET_NULL)
    
    rating = models.IntegerField(default=0)
    review = models.TextField( blank=True ) 


    @property
    def rating_is(self):
        new_rating = 0
        rating_obj = rating_review.objects.filter(doctor=self.doctor)
        for i in rating_obj:
            new_rating += i.rating
       
        new_rating = new_rating/len(rating_obj)
        new_rating = int(new_rating)
        
        return new_rating