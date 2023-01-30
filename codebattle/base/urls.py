from django.urls import path
from.import views

urlpatterns =[
    path('',views.home_page,name='home'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.logout_page,name='logout'),
    path('user/<str:pk>/',views.user_page,name='profile'),
    path('event/<str:pk>/',views.event_page,name = 'event'),
    path('event_confirmation/<str:pk>/',views.registration_confirmation,name = 'event_confirmation'),
    path('account/',views.account_page,name='account'),
    path('project_submission/<str:pk>/',views.project_submission,name='project_submission'),
    path('update_submission/<str:pk>/',views.update_submission,name='update_submission'),
    path('images/<str:pk>/',views.update_submission,name='update_submission'),
]





