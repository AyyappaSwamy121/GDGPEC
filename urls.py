from django.urls import path
from . import views

urlpatterns = [
    path('member/',views.member, name='member'), 
    path('login2/',views.login2, name='login2'), 
    path('registration/',views.registration, name='registration'), 
    path('registration_adding/',views.registration_adding, name='registration_adding'), 
    path('user_login/',views.user_login, name='user_login'), 
    path('after_login/',views.after_login, name='after_login'), 
    path('quiz_instruction/',views.quiz_instruction, name='quiz_instruction'), 
    # path('quiz_template/',views.kaggle, name='kaggle'), 
    path('kaggle/',views.kaggle, name='kaggle'), 
    path('contact/',views.contact, name='contact'), 
    path('after_login/',views.after_login, name='after_login'), 
    path('gallery2/',views.gallery2, name='gallery2'), 
    path('home/',views.home, name='home'), 
    path('perks/',views.perks, name='perks'), 
    path('a/',views.a, name='a'), 
    path('view_score/',views.view_score, name='view_score'), 
    path('quiz/<str:quiz_name>/', views.quiz_view, name='quiz'),
]