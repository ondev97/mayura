# Generated by Django 3.2 on 2021-05-14 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayuraweb', '0011_contactus_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_content_2_in_quotation',
            field=models.BooleanField(default=False),
        ),
    ]
