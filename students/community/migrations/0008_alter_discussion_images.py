# Generated by Django 3.2.20 on 2023-10-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_discussion_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='images',
            field=models.ImageField(null=True, upload_to='static/'),
        ),
    ]
