# Generated by Django 3.2.2 on 2021-05-14 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brows', '0003_auto_20210514_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Комментарий преподавателя'),
        ),
    ]
