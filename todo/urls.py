from django.contrib import admin
from django.urls import path

from todolist.views import todo, redirect_view, category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo, name='todo'),
    path('category/', category, name='category'),
    path('', redirect_view),
]
