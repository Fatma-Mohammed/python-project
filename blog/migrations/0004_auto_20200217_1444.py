# Generated by Django 3.0.3 on 2020-02-17 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200217_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='checkPassword',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64),
        ),
    ]
