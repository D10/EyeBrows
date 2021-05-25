from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Lessons, Answers, Photos


class PhotoTabularAdmin(admin.TabularInline):
    model = Photos


class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'Video', 'abstract', 'home_work')
    save_on_top = True


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_answer', 'from_lesson', 'comments', 'is_correct')
    list_display_links = ('id', 'user_answer', 'from_lesson')
    inlines = [PhotoTabularAdmin]
    save_on_top = True


class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'answer')
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50">')

    get_image.short_description = 'Изображение'


admin.site.register(Photos, PhotosAdmin)
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Answers, AnswersAdmin)
