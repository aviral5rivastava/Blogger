# Generated by Django 4.2.15 on 2024-09-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.TextField(default='untitled', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]