# Generated by Django 3.2.2 on 2021-05-13 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brows', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'ordering': ['pk'], 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
    ]
