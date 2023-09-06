# Generated by Django 4.2.1 on 2023-07-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_appointment_appointment_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctormodel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patientmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment_patient',
        ),
    ]
