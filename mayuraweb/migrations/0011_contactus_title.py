# Generated by Django 3.2 on 2021-05-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayuraweb', '0010_blogpost_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
