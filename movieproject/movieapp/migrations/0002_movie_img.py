# Generated by Django 3.2.12 on 2022-02-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='darsh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
