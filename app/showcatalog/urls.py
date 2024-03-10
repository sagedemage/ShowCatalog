from django.urls import path
from showcatalog.views.pages import *
from showcatalog.views.show import *

urlpatterns = [
    # Pages
    path('', index, name='index'),
    path('about', about, name='about'),
    path('dashboard', dashboard, name='dashboard'),
    path('update-show', update_show_page, name='update_show_page'),
    path('add-show', add_show_page, name='add_show'),

    # Show APIs
    path('api/add-show', add_show, name='add_show'),
    path('api/update-show', update_show, name='update_show'),
    path('api/delete-show', delete_show, name='delete_show'),
    path('api/fetch-show', fetch_show, name='fetch_show'),
]