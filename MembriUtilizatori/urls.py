from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordsChangeView
from django.contrib.auth import views as auth_views
from .import views


urlpatterns = [
	
	path('register/', UserRegisterView.as_view(), name = 'register'),
	path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
	path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
	path('password_succes', views.password_succes, name = 'password_succes'),
	#path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
]
