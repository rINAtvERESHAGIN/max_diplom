from django.urls import include, path
from polls import views
from polls.views import AddNewMusic

urlpatterns = [
    path('add_music1/', views.add_music),
    path('add_music/', AddNewMusic.as_view()),
    path('update_post/<str:id>', views.update_post),
    path('delete_post/<str:id>', views.delete_post),
    path('read_post/<str:id>', views.read_post),
    path('get_all_music/', views.get_all_music),
]
