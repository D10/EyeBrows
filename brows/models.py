from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q


class Lessons(models.Model):
    lesson = models.CharField(max_length=250, verbose_name='Урок')
    Video = models.CharField(max_length=250, verbose_name='Видео')
    abstract = models.TextField(verbose_name='Конспект')
    home_work = models.TextField(verbose_name='Домашнее задание')

    def __str__(self):
        return f'{self.lesson}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('lessons_detail', kwargs={'pk': self.pk})


class Answers(models.Model):
    user_answer = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='Пользователь')
    from_lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='Урок')
    # answer = models.ImageField(verbose_name='Ответ')
    comments = models.TextField(verbose_name='Комментарий преподавателя', blank=True)
    is_correct = models.BooleanField(default=0, verbose_name='Допуск к следующему уроку')

    def __str__(self):
        return f'{self.user_answer}'

    def get_absolute_url(self, from_lesson):
        return reverse('lessons_detail', kwargs={'pk': from_lesson.pk})

    def lesson_prev(self, lesson_next):
        prev_lesson = Lessons.objects.filter(pk__lt=lesson_next).order_by('-pk').first()
        lesson_previous = Answers.objects.filter(
            Q(user_answer=self.user_answer) & Q(from_lesson=prev_lesson)).first()
        return lesson_previous.is_correct

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['pk']


class Photos(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Ответ')
    answer = models.ForeignKey(Answers, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer}'

    def get_absolute_url(self):
        return reverse('lessons_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['pk']
