from django.urls import URLPattern, path

from .views import (
    homeView
)

urlpatterns=[
    path('listex',homeView)
]