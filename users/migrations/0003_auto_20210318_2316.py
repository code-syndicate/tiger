# Generated by Django 3.1.6 on 2021-03-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
    ]