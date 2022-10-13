from django.contrib import admin
from django.urls import path,  include # добавили подключение страницы
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls as auth_urls
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('', include('main.urls', namespace='main'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



