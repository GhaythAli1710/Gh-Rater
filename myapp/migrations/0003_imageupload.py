# Generated by Django 4.0.4 on 2022-05-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_uploadimagetest'),
    ]

    operations = [
        migrations.CreateModel(
            name='imageupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to='', verbose_name='images')),
            ],
        ),
    ]
