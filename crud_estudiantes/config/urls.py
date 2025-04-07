from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estudiantes.urls')),  # 👈 Aquí enlazas las URLs de tu app
]