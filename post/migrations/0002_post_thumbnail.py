# Generated by Django 2.2.7 on 2019-11-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='TEST', upload_to=''),
            preserve_default=False,
        ),
    ]