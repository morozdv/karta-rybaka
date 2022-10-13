from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    
    path('', views.home_page, name='home'),
    path('get-fishings/', views.get_fisings, name='get-fishings'),
    path('save-fishing/', views.save_fishing, name='save-fishing'),

]







