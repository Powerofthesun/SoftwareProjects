# Generated by Django 2.0.1 on 2018-03-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_auto_20180313_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='bio1',
        ),
        migrations.AddField(
            model_name='candidate',
            name='bio2',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
