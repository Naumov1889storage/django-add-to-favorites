from django.urls import include, path
from favorites.views import favorites_list, add_to_favorites, remove_from_favorites, delete_favorites


app_name = 'favorites'
urlpatterns = [
    path('', favorites_list, name='list'),
    path('<id>/add/', add_to_favorites, name='add'),
    path('<id>/remove/', remove_from_favorites, name='remove'),
    path('delete/', delete_favorites, name='delete'),
]
