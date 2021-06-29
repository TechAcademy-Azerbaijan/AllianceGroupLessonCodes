from django.urls import path, re_path
from accounts.views import (
    login,
    logout,
    register,
    activate,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='confirmation'),
    path('register/', register, name='register'),
]
