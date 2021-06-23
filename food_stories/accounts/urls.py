from django.urls import path
from accounts.views import (
    login,
    logout,
    register,
    activate
)

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('register/', register, name='register'),
]
