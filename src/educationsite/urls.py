from django.contrib import admin
from django.urls import path, include

from educationsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/signup/', views.signup_view, name='signup'),
    path('account/login/', views.login_view, name='login'),
    path('account/logout/', views.logout_view, name='logout'),
    path('reminder/', include("reminder.urls"))
]
