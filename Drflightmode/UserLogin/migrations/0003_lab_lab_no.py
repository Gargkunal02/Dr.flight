# Generated by Django 4.0.3 on 2022-03-14 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserLogin', '0002_alter_doctor_photo_alter_patient_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='lab_no',
            field=models.CharField(default='1221', max_length=30),
        ),
    ]
