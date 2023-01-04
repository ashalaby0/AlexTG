# Generated by Django 4.1.3 on 2023-01-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, upload_to='photo/ride')),
                ('no_of_bags', models.IntegerField()),
                ('no_of_passengers', models.IntegerField()),
            ],
        ),
    ]
