from django.urls import path
from App_Login import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
    path('add_profile_pic/', views.add_profile_pic, name='add_profile_pic'),
    path('change_profile_pic/', views.change_profile_pic, name='change_profile_pic'),
]
