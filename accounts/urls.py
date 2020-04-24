from django.urls import path, include
from .views import user_login, user_logout, user_account, user_registration,        edit_account
from accounts import url_reset


urlpatterns = [
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('account/', user_account, name="account"),
    path('register/', user_registration, name="registration"),
    path('edit/', edit_account, name="edit_account"),
    path('reset-password/', include(url_reset))
]
