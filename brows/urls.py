from django.urls import path

from .views import home, user_contact, LessonsDetail, lessons_list, user_logout, lessons_detail

urlpatterns = [
    path('', home, name='home'),
    path('email/', user_contact, name='send_mail'),
    path('lessons/', lessons_list, name='lessons_list'),
    path('lessons/<int:pk>/', lessons_detail, name='lessons_detail'),
    path('logout/', user_logout, name='logout'),
]
