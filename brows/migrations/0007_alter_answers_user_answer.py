# Generated by Django 3.2.2 on 2021-05-14 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brows', '0006_alter_answers_from_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='user_answer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]