# Generated by Django 2.0.1 on 2018-03-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_solicit', '0020_auto_20180317_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_invitation',
            name='uuid',
            field=models.CharField(default='BLDCD', max_length=5, primary_key=True, serialize=False),
        ),
    ]
