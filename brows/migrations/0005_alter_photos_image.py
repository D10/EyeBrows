# Generated by Django 3.2.2 on 2021-05-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brows', '0004_alter_answers_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Ответ'),
        ),
    ]