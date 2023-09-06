from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model ()

# Create your models here.


class DoctorModel(models.Model):
    dr_name = models.CharField(max_length=200)
    dr_image = models.ImageField(upload_to="image/", null=True)
    dr_department = models.CharField(max_length=200)
    dr_time = models.CharField(max_length=200)
    dr_phone = models.CharField(max_length=10,null=True)


class PatientModel(models.Model):
    patient=models.ForeignKey(user,on_delete= models.CASCADE,null= True)
    p_name = models.CharField(max_length=200)
    p_address = models.CharField(max_length=200)
    gender = models.CharField(max_length=200,null=True)
    p_phone = models.CharField(max_length=10,null=True)
    p_age = models.IntegerField()
    p_blood = models.CharField(max_length=300)
    p_image=models.ImageField(upload_to="image/",null=True)
    join_date = models.DateField(auto_now_add=True)



class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id
    
class Appointment(models.Model):
    Doctor_id = models.ForeignKey(DoctorModel, on_delete=models.CASCADE, null=True)
    patient_id = models.ForeignKey(PatientModel, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    status=models.BooleanField(default=True)
    appointment_status=models.BooleanField(default=False)

    # def __str__(self):
    #     return self.Doctor_id

    class Meta:
        # Set the custom table name to 'app_appointment'
        db_table = 'app_appointment'

class DischargeModel(models.Model):
    name=models.ForeignKey(PatientModel,on_delete= models.CASCADE,null= True)
    releaseDate=models.DateField(null=False)
    medicine_cost=models.PositiveIntegerField(null=False)
    room_rent=models.PositiveIntegerField(null=False)
    gst=models.FloatField(null=False)
    total_cost=models.FloatField(null=False)


