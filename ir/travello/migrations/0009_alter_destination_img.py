# Generated by Django 3.2 on 2021-06-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0008_alter_destination_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
