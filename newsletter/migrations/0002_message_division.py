# Generated by Django 4.0.4 on 2022-05-19 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_member_division_member_division'),
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.division'),
        ),
    ]
