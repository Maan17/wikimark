from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<title>', views.entry_detail, name='entry_detail'),
    path('search/',views.search, name='search'),
    path('new/',views.new_page,name='new_page'),
    path('<title>/edit/',views.edit_page,name='edit_page'),
    path('random_entry/',views.random_entry,name='random_entry'),
]
