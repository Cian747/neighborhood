# Generated by Django 3.2.7 on 2021-09-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='family_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
