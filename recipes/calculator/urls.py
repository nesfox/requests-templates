from django.urls import path
from .views import recipe_view

urlpatterns = [
    path('<slug:dish>/', recipe_view),
]