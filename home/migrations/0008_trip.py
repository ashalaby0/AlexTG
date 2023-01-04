# Generated by Django 4.1.3 on 2023-01-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_customermessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]