from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.index, name="index")
]
=======
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry, name="entry"),
    path("search", views.search, name = "search"),
    path("createEntry", views.createEntry, name="createEntry"),
    path("wiki/<str:name>/edit", views.edit, name="edit"),
     path("randomPage", views.randomPage, name="randomPage"),
] 
>>>>>>> 377c1a4 (modified views, urls and templates)
