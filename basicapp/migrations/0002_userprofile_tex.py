# Generated by Django 3.0.4 on 2020-03-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tex',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]