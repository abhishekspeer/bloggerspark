# Modules
from django.urls import path
from . import views

# urlconfig

urlpatterns = [
    path('', views.post_list, name = "post_list"),
    # to /'' url, post from views i.e post view from view module. name(identity) of url is post_list

]
