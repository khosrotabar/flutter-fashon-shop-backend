from django.urls import path
from . import views

urlpatterns = [
    path('toggle/', views.ToggleWishList.as_view(), name='add-remove-from-whishlist'),
    path('me/', views.GetWhishList.as_view(), name='get-whishlist'),
]