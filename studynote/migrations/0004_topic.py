# Generated by Django 2.2.5 on 2022-01-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studynote', '0003_auto_20220126_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
