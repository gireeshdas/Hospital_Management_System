# Generated by Django 4.2.1 on 2023-07-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_patientmodel_p_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='dr_phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
