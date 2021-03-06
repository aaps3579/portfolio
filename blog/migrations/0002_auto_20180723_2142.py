# Generated by Django 2.0.7 on 2018-07-23 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]
