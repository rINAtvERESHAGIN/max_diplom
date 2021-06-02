from django.urls import include, path

urlpatterns = [
    path('add_music/', include('max_diplom.urls')),
    path('get_all_music/', include('max_diplom.urls')),
]
