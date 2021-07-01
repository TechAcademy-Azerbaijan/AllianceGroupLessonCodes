from django.urls import path, re_path
from accounts.views import (
    CustomLoginView,
    logout,
    RegisterView,
    activate,
    UserProfileView, CustomPasswordResetView, CustomPasswordResetConfirmView
)

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='confirmation'),
    re_path(r'reset-password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            CustomPasswordResetConfirmView.as_view(), name='reset-password'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forget-password/', CustomPasswordResetView.as_view(), name='password-reset-view'),
    path('user-profile/<int:pk>/', UserProfileView.as_view(), name='user-profile')
]
