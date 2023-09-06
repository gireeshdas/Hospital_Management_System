from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name="home"),
    path("login_page",views.login_page,name="login_page"),
    path('Please_login',views.Please_login,name="Please_login"),
    path("signup_page",views.signup_page,name="signup_page"),
    path("about_page",views.about_page,name="about_page"),


    path("AdminLandingPage",views.AdminLandingPage,name="AdminLandingPage"),
    path("PatientLandingPage",views.PatientLandingPage,name="PatientLandingPage"),

    path("Login",views.Login,name="Login"),
    path("logout",views.logout,name="logout"),

    path("speciality_page",views.speciality_page,name="speciality_page"),

    path("create_user",views.create_user,name="create_user"),
    # path("send_confirmation_email",views.send_confirmation_email,name="send_confirmation_email"),
    path("add_doctor_page",views.add_doctor_page,name="add_doctor_page"),
    path("Add_doctor",views.Add_doctor,name="Add_doctor"),

    path("profile",views.profile,name="profile"),
    path('edituser/<int:userId>',views.edituser,name='edituser'),
    path('updateuser/<int:userId>',views.updateuser,name='updateuser'),

    path("admin_patient",views.admin_patient,name="admin_patient"),
    path("delete_patient/<int:pk>",views.delete_patient,name="delete_patient"),

    path("admin_doctor",views.admin_doctor,name="admin_doctor"),
    path("edit_doctor_page/<int:pk>",views.edit_doctor_page,name="edit_doctor_page"),
    path("edit_doctor/<int:pk>",views.edit_doctor,name="edit_doctor"),
    path("delete_doctor/<int:pk>",views.delete_doctor,name="delete_doctor"),
    path("patient_doctor_list",views.patient_doctor_list,name="patient_doctor_list"),

    path('contact',views.contact,name="contact"),
    path('open_enquiry',views.open_enquiry,name="open_enquiry"),
    path('read_queries', views.read_queries, name='read_queries'),
    path('view_queries/<int:pid>',views.view_queries, name='view_queries'),
    path('unread_queries', views.unread_queries, name='unread_queries'),


    path("discharge_page",views.discharge_page,name="discharge_page"),
    path("discharge_patient/<int:pk>",views.discharge_patient,name="discharge_patient"),
    path("discharge_bill/<int:pk>",views.discharge_bill,name="discharge_bill"),

    path("patient_view_bill/<int:pk>",views.patient_view_bill,name="patient_view_bill"),



    path("appointment_page",views.appointment_page,name="appointment_page"),
    path("create_appointment/<int:pk>",views.create_appointment,name='create_appointment'),
    path("admin_appointment",views.admin_appointment,name="admin_appointment"),
    path("confirm_appointment/<int:pk>",views.confirm_appointment,name="confirm_appointment"),

    path("patient_appointment_details/<int:pk>",views.patient_appointment_details,name="patient_appointment_details"),
     path('change_password/', views.change_password, name='change_password'),

]

# def new_func():
#     handler404 = 'app.views.error_404_view'

# new_func()
