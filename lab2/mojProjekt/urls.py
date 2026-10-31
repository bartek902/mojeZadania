from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Zakomentowałem starą aplikację:
    # path('', include('witaj.urls')),

    # Podpinam nową aplikację z laboratorium pod stronę główną:
    path('', include('frontend_demo.urls')),
]