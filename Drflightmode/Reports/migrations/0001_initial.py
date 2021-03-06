# Generated by Django 4.0.3 on 2022-03-14 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestDetails', '0002_alter_testdetail_testtype'),
        ('UserLogin', '0002_alter_doctor_photo_alter_patient_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientTestDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=50)),
                ('dateTimeCollection', models.DateTimeField(auto_now_add=True)),
                ('dateTimeReceived', models.DateTimeField(auto_now=True)),
                ('dateTimeReported', models.DateTimeField()),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserLogin.patient')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestDetails.testdetail')),
            ],
        ),
        migrations.CreateModel(
            name='OneTimeTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestInput', models.ManyToManyField(to='Reports.patienttestdetail')),
            ],
        ),
    ]
