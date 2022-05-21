from django.urls import re_path

from . import views

size = r'(?P<width>\d{1,4})(x(?P<height>\d{1,4}))?'
ext = r'(?P<ext>.(jpg|jpeg|png))?'
background = r'(?P<background>([0-9a-fA-F]{3}){1,2})'
foreground = r'(?P<foreground>([0-9a-fA-F]{3}){1,2})'

urlpatterns = [
    re_path(f'^{size}{ext}/$', views.placeholder),
    re_path(f'^{size}{ext}/{background}/$', views.placeholder),
    re_path(f'^{size}{ext}/{background}/{foreground}/$', views.placeholder),
]
