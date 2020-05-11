from django.urls import include, path
from base.views import home_page

urlpatterns = [
    path('', home_page)
]
