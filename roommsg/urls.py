

from django.urls import path
from roommsg import views
urlpatterns = [
    path("<int:room_num>", views.room_msg),


]