# Generated by Django 4.0.4 on 2022-05-20 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='accepted',
            name='accepted',
            field=models.BooleanField(null=True),
        ),
    ]
