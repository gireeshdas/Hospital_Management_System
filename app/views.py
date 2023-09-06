import email
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from app import models
from app.models import Appointment, DoctorModel,PatientModel,Contact, DischargeModel
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from datetime import date, datetime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# Create your views here.


def error_404_view(request,exception):
    return render(request,"404.html",status=404)


def home(request):
    return render(request,"home.html")

def login_page(request):
    return render(request,"login_page.html")

def Please_login(request):
    return render(request,"please_login.html")

def signup_page(request):
    doctor=DoctorModel.objects.all()
    context={'doctor':doctor}
    return render(request,"signup_page.html",context)

def about_page(request):
    return render(request,"about.html")

def AdminLandingPage(request):
    return render(request,"admin_home.html")

def PatientLandingPage(request):
    return render(request,"patient_home.html")

def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password'] 
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if(user.is_superuser):
                messages.info(request,"Login successed!")
                return redirect('AdminLandingPage')
            else:
                request.session['uid']=user.id
                messages.info(request,"Login successed!")
                return redirect('PatientLandingPage')
        else:
            messages.info(request,"invalid username and password")
            return redirect('login_page')
    else:
        return redirect('login_page')
    
def logout(request):
	auth.logout(request)
	return redirect('home')

def speciality_page(request):
    return render(request,"spec.html")

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# def create_user(request):
#     if request.method == "POST":
#         p_name = request.POST["p_name"]
#         update_type = request.POST.get('gender')
#         if update_type == "Male":
#             gender = "Male"
#         else:
#             gender = "Female"

#         p_address = request.POST["p_address"]
#         p_phone = request.POST['p_phone']
#         p_age = request.POST["p_age"]
#         p_blood = request.POST['p_blood']
#         email = request.POST["email"]
#         username = request.POST["username"]
#         password = request.POST["password"]
#         cpassword = request.POST["cpassword"]

#         p_image = request.FILES.get('file')
#         if p_image is None:
#             p_image = 'image/img.png'

#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "This username is already taken, try another.")
#                 return redirect("signup_page")
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, "This email is already in use.")
#                 return redirect("signup_page")
#             else:
#                 user = User.objects.create_user(username=username, password=password, email=email)
#                 user.save()
#                 data = User.objects.get(id=user.id)
#                 patient_data = PatientModel(
#                     p_name=p_name,
#                     gender=gender,
#                     p_age=p_age,
#                     p_address=p_address,
#                     p_phone=p_phone,
#                     patient=data,
#                     p_blood=p_blood,
#                     p_image=p_image,
#                 )
#                 patient_data.save()
                
#                 # Sending a confirmation email to the user
#                 subject = "Registration Completed"
#                 message = f"Dear {p_name},\nYour account has been successfully created. \nUsername: {username}\nPassword: {password}"
#                 recipient = email
#                 send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                
#                 messages.success(request, 'Registration is successful')
#                 return redirect("login_page")
#         else:
#             messages.error(request, "Passwords do not match. Try again.")
#             return redirect('signup_page')
#     else:
#         return redirect('signup_page')

import random
import string

# ... (existing imports and code)

def generate_random_password():
    """Generate a random password with 8 characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(8))

def create_user(request):
    if request.method == "POST":
        p_name = request.POST["p_name"]
        update_type = request.POST.get('gender')
        if update_type == "Male":
            gender = "Male"
        else:
            gender = "Female"

        p_address = request.POST["p_address"]
        p_phone = request.POST['p_phone']
        p_age = request.POST["p_age"]
        p_blood = request.POST['p_blood']
        email = request.POST["email"]
        username = request.POST["username"]
        p_image = request.FILES.get('file')
        if p_image is None:
            p_image = 'image/img.png'

        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken, try another.")
            return redirect("signup_page")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "This email is already in use.")
            return redirect("signup_page")
        else:
            # Generate a random password for the user
            password = generate_random_password()

            # Create the user without setting the password yet
            user = User.objects.create_user(username=username, password=None, email=email)
            user.save()

            # Set the auto-generated password for the user
            user.set_password(password)
            user.save()

            data = User.objects.get(id=user.id)
            patient_data = PatientModel(
                p_name=p_name,
                gender=gender,
                p_age=p_age,
                p_address=p_address,
                p_phone=p_phone,
                patient=data,
                p_blood=p_blood,
                p_image=p_image,
            )
            patient_data.save()

            # Sending a confirmation email to the user
            subject = "Registration Completed"
            message = f"Dear {p_name},\nYour account has been successfully created. \nUsername: {username}\nPassword: {password}"
            recipient = email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)

            messages.success(request, 'Registration is successful')
            return redirect("login_page")
    else:
        return redirect('signup_page')
    
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        confirm_new_password = request.POST["confirm_new_password"]

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, "Incorrect old password. Please try again.")
            return redirect("change_password")

        if new_password != confirm_new_password:
            messages.error(request, "New passwords do not match. Please try again.")
            return redirect("change_password")

        # Set the new password and update the session auth hash
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Update the session to prevent logout

        messages.success(request, "Password changed successfully.")
        return redirect("profile")

    return render(request,"change_password.html")

  
def add_doctor_page(request):
    return render(request,"add_doctor.html")
    
def Add_doctor(request):
    if request.method=="POST":
        dr_name=request.POST["dr_name"]
        dr_department=request.POST["dr_department"]

        update_type=request.POST.get('dr_time')
        if update_type=="Day":
            dr_time="Day"
        elif update_type=="Night" :
            dr_time="Night"
        else:
            dr_time="Off"
        

        dr_phone=request.POST["dr_phone"]
        dr_image=request.FILES.get('file')
        if dr_image==None:
            dr_image='image/img.png'
        

        data=DoctorModel(dr_name=dr_name,dr_department=dr_department,dr_image=dr_image,dr_time=dr_time,dr_phone=dr_phone)
        data.save()
        messages.info(request,"Added a new doctor")
        return redirect("AdminLandingPage")
    
def profile(request):
    if 'uid' in request.session:
        userId = request.session['uid']
        user = PatientModel.objects.get(patient=userId)
        return render(request,'profile.html',{'user':user})
    else:
        return redirect('login_page')

def edituser(request,userId):
    user= PatientModel.objects.get(patient=userId)
    context={'user':user,}
    return render(request,'edituser.html',context)

def updateuser(request,userId):
    user=User.objects.get(id=userId)
    patient=PatientModel.objects.get(patient=userId)

    if request.method == 'POST':
        user.email=request.POST["email"]
        user.save()

        patient.p_name=request.POST["p_name"]
        patient.p_age=request.POST["p_age"]
      
        patient.p_address=request.POST["p_address"]
        patient.p_phone=request.POST["number"]
        patient.p_blood=request.POST['p_blood']

        update_type = request.POST.get('gender')
        if update_type == 'Male':
            patient.gender = "Male"
        else:
            patient.gender = "Female"

        old=patient.p_image
        new=request.FILES.get('file')
        if old !=None and new==None:
            patient.p_image=old
        else:
            patient.p_image=new
        patient.save()
        messages.info(request,"Your profile has been updated")

        return redirect('profile')
    
    else: 
        return redirect('Login')
    
def admin_patient(request):
    patient=PatientModel.objects.all()
    user=User.objects.all()
    context={'patient':patient,'user':user}
    return render(request,"admin_patient.html",context)

def delete_patient(request,pk):
    patient=PatientModel.objects.get(id=pk)
    patient.delete()
    return redirect("admin_patient")

def admin_doctor(request):
    doctor=DoctorModel.objects.all()
    context={'doctor':doctor}
    return render(request,"admin_doctor.html",context)


def edit_doctor_page(request,pk):
    doctor=DoctorModel.objects.get(id=pk)
    context={'doctor':doctor}
    return render(request,"edit_doctor.html",context)

def edit_doctor(request,pk):
    doctor=DoctorModel.objects.get(id=pk)
    if request.method=="POST":
        doctor.dr_name=request.POST['dr_name']
        doctor.dr_phone=request.POST['dr_phone']

        update_type = request.POST.get('gender')
        if update_type == 'Day':
            doctor.dr_time = "Day"

        elif update_type=="Night":
            doctor.dr_time = "Night"
        else:
            doctor.dr_time = "Off"

        old=doctor.dr_image
        new=request.FILES.get('file')
        if old !=None and new==None:
            doctor.dr_image=old
        else:
            doctor.dr_image=new
        doctor.save()
        messages.info(request,"Updated your changes")
        return redirect("admin_doctor")
    else:
        return redirect("edit_doctor_page")
    
def delete_doctor(request,pk):
    doctor=DoctorModel.objects.get(id=pk)
    doctor.delete()
    return redirect("admin_doctor")

    
def patient_doctor_list(request):
    doc=DoctorModel.objects.all()
    context={'doc':doc}
    return render(request,'patient_doc_list.html',context)


def contact(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        try:
            Contact.objects.create(name=n, contact=c, email=e, subject=s, message=m, msgdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def open_enquiry(request):
    return render(request,"open_enquiry.html")

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="yes")
    return render(request,'read_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request,'view_queries.html', locals())

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html', locals())


def discharge_page(request):
    patient=PatientModel.objects.all()
    context={'patient':patient}
    return render(request,"discharge_patient_view.html",context)

def discharge_patient(request,pk):
    patient=PatientModel.objects.filter(id=pk)
    context={'patient':patient}
    return render(request,"discharge_page.html",context)

def discharge_bill(request,pk):
    name=PatientModel.objects.get(id=pk)
    if request.method=="POST":
        releaseDate=request.POST['releaseDate']
        medicine_cost=request.POST['medicine_cost']
        room_rent=request.POST['room_rent']
        gst=request.POST['gst']
        total_cost=request.POST['total_cost']
        request.session['uid']=name.id

        discharge=DischargeModel(
            name=name,
            releaseDate=releaseDate,
            medicine_cost=medicine_cost,
            room_rent=room_rent,
            gst=gst,
            total_cost=total_cost,
        )
        discharge.save()
        # messages.info(request,"Bill created")
        return redirect("discharge_page")
    else:
        return redirect("discharge_page")
    
def patient_view_bill(request,pk):
    user=PatientModel.objects.all()
    app=DischargeModel.objects.filter(id=pk)
    context={'app':app,'user':user}
    return render(request,"patient_bill.html",context)


def appointment_page(request):
 doctor=DoctorModel.objects.all()
 context={'doctor':doctor}
 return render(request,"appointment_page.html",context)


def create_appointment(request,pk):
    try:
        patient_id=PatientModel.objects.get(patient_id=pk) 
    except PatientModel.DoesNotExist:
        patient_id = None

    # patient_id=PatientModel.objects.get(id=pk) 
    # print("primary key--",pk)
    pdata = PatientModel.objects.filter(patient_id=pk).values()
    # print(pdata)

    if request.method == 'POST':
        doctor_id = request.POST.get('select')
        date = request.POST.get('date')
        time = request.POST.get('time')
        # request.session['uid']=patient_id.id 
        #        
        # patient_id = request.session['uid']
        # print("patient_id--",patient_id)
        appointment = Appointment(
            Doctor_id_id=doctor_id,
            patient_id=patient_id,
            date=date,
            time=time,
        )
        
        appointment.save()
        messages.info(request,"successfully created!")
        return redirect('PatientLandingPage')
    else:
        return redirect('appointment_page')


def admin_appointment(request):
    appointment=Appointment.objects.all()
    context={'appointment':appointment}
    return render(request,"admin_appointment.html",context)
    
def confirm_appointment(request,pk):
    confirmobj=Appointment.objects.get(id=pk)    
    confirmobj.appointment_status = True
    confirmobj.save()
    messages.info(request,"Patient appointment has been Approved")
    # pdata = PatientModel.objects.filter(patient_id=pk).values()
    # print(pdata)
    # doctor.delete()
    return redirect("admin_appointment") 

def patient_appointment_details(request,pk):
    app=Appointment.objects.filter(id=pk)
    context={'app':app}
    return render(request,"patient_appointment_view.html",context)









 



















    



