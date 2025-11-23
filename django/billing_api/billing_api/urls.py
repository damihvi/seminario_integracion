# billing_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),      # Autenticación y usuarios
    path('api/', include('catalog.urls')),    # Catálogo (categorías, productos)
    path('api/', include('invoices.urls')),   # Facturas
    path('api/', include('warehouses.urls')), # Almacenes
]