# Generated by Django 2.0.2 on 2018-03-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_solicit', '0005_auto_20180310_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_invitation',
            name='uuid',
            field=models.CharField(default='LTK7P', max_length=5, primary_key=True, serialize=False),
        ),
    ]