from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/home', views.HomeCategoryList.as_view(), name='home-category-list'),
    path('', views.ProductCategoryList.as_view(), name='product-category-list'),
    path('popular/', views.PopularProductsList.as_view(), name='popular-category-list'),
    path('byType/', views.ProductsListByClothesType.as_view(), name='list-by-type'),
    path('search/', views.SearchProductsByTitle.as_view(), name='search'),
    path('category/', views.FilterProductsByCategory.as_view(), name='product-by-category'),
    path('recomendations/', views.SilmilarProducts.as_view(), name='similar-products'),
]