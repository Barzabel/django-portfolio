# Generated by Django 4.1.1 on 2022-09-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_data_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog/images'),
        ),
    ]