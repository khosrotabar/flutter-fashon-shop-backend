from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/products/', include('core.urls')),
    path('api/whishlist/', include('whishlist.urls')),
    path('api/cart/', include('cart.urls'))
]
