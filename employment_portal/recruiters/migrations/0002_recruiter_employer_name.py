# Generated by Django 2.0.1 on 2018-03-17 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_employer_website'),
        ('recruiters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='Employer_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Employer'),
        ),
    ]
