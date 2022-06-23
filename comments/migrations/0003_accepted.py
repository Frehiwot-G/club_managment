# Generated by Django 4.0.4 on 2022-05-19 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000, null=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comments.comment')),
            ],
        ),
    ]