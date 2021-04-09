from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create new person"),
    path('update/', views.update, name="update a person"),
    path('rating/', views.add_ratings, name="add ratings"),
    # path('getall/', views.getallpersons, name="get all person objects"),
]
