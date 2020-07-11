from django.urls.conf import path
from . import views

urlpatterns = [
    path("user", views.testing),
    path("check_user", views.check_user),
    path("change_pwd", views.change_pwd),
    path("forget_pwd", views.forget_pwd),
    path("logout", views.logout),
]